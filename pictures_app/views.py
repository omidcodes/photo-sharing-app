from django.shortcuts import render, redirect

from pictures_app.utils import upload_picture_to_azure
from .models import PictureModel, Rating

from .forms import CommentForm, RatingForm
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.contrib import messages
from django.core.paginator import Paginator

from django.core.cache import cache
from django.views.decorators.cache import never_cache
from django.conf import settings


GALLERY_CACHE_KEY = "enriched_gallery_data"


@login_required
def upload_picture(request):
    if request.method == "POST" and request.FILES.get("picture"):
        picture = request.FILES["picture"]
        picture_url = upload_picture_to_azure(picture)

        name: str = picture.name
        caption = request.POST.get("caption")
        location = request.POST.get("location")
        title = name
        creator = request.user

        PictureModel.objects.create(
            title=title,
            caption=caption,
            location=location,
            picture_url=picture_url,
            creator=creator,
        )

        # ✅ Invalidate the gallery cache
        cache.delete(GALLERY_CACHE_KEY)

        messages.success(request, "Picture uploaded successfully!")
        return redirect("view_galleries")

    return render(request, "upload_picture.html")


@never_cache
@login_required
def view_galleries(request):
    """
    cache.get() / cache.set()	To store and reuse enriched gallery data
    @never_cache	Prevents Django from caching the response to POST submissions
    Caching only happens in GET mode	Avoids conflicts with rating/comment updates
    Timeout set to 300 seconds (5 mins)	You can adjust as needed
    """
    if request.method == "POST":
        picture_id = request.POST.get("picture_id")
        picture = PictureModel.objects.get(id=picture_id)

        if "rating_submit" in request.POST:
            rating_form = RatingForm(request.POST)
            if rating_form.is_valid():
                existing_rating = Rating.objects.filter(
                    user=request.user, picture=picture
                ).first()
                if existing_rating:
                    existing_rating.score = rating_form.cleaned_data["score"]
                    existing_rating.save()
                else:
                    rating = rating_form.save(commit=False)
                    rating.user = request.user
                    rating.picture = picture
                    rating.save()

                cache.delete(GALLERY_CACHE_KEY)  # Invalidate cache after rating

        elif "comment_submit" in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.picture = picture
                comment.save()

                cache.delete(GALLERY_CACHE_KEY)  # Invalidate cache after comment

        return redirect("view_galleries")

    enriched_pictures = cache.get(GALLERY_CACHE_KEY)

    if not enriched_pictures:
        pictures = PictureModel.objects.all()
        enriched_pictures = []

        for pic in pictures:
            average_rating = pic.ratings.aggregate(Avg("score"))["score__avg"]
            comments = pic.comments.order_by("-timestamp")
            enriched_pictures.append(
                {
                    "picture": pic,
                    "average_rating": average_rating,
                    "rating_form": RatingForm(),
                    "comment_form": CommentForm(),
                    "comments": comments,
                }
            )

        # Cache for CACHE_TIMEOUT minutes
        cache.set(GALLERY_CACHE_KEY, enriched_pictures, timeout=settings.CACHE_TIMEOUT)

    paginator = Paginator(enriched_pictures, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "view_galleries.html", {"page_obj": page_obj})
