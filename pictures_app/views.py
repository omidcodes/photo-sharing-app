from django.shortcuts import render, redirect, get_object_or_404

from pictures_app.utils import upload_picture_to_azure
from .models import PictureModel, Comment, Rating
from .forms import PictureForm, CommentForm, RatingForm
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from .models import PictureModel, Comment, Rating
from .forms import CommentForm, RatingForm
from django.shortcuts import render, redirect
from django.contrib import messages



@login_required
def upload_picture(request):
    if request.method == 'POST' and request.FILES.get('picture'):
        picture = request.FILES['picture']
        # Upload picture to Azure Blob Storage
        picture_url = upload_picture_to_azure(picture)

        # e.g : mypic01.jpg -> mypic01
        name :str = request.FILES['picture'].name

        caption = request.POST.get('caption')
        location = request.POST.get('location')
        title = name
        creator = request.user

        PictureModel.objects.create(title=title, caption=caption, location=location, picture_url=picture_url, creator=creator)
        messages.success(request, 'Picture uploaded successfully!')
        return redirect('view_galleries')
    return render(request, 'upload_picture.html')




@login_required
def view_galleries(request):
    if request.method == 'POST':
        picture_id = request.POST.get('picture_id')
        picture = PictureModel.objects.get(id=picture_id)

        if 'rating_submit' in request.POST:
            rating_form = RatingForm(request.POST)
            if rating_form.is_valid():
                rating = rating_form.save(commit=False)
                rating.user = request.user
                rating.picture = picture
                rating.save()

        elif 'comment_submit' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.picture = picture
                comment.save()

        return redirect('view_galleries')

    pictures = PictureModel.objects.all()
    enriched_pictures = []

    for pic in pictures:
        average_rating = pic.ratings.aggregate(Avg('score'))['score__avg']
        comments = pic.comments.order_by('-timestamp')
        enriched_pictures.append({
            'picture': pic,
            'average_rating': average_rating,
            'rating_form': RatingForm(),
            'comment_form': CommentForm(),
            'comments': comments
        })

    return render(request, 'view_galleries.html', {'gallery': enriched_pictures})
