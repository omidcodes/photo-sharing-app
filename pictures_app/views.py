from django.shortcuts import render, redirect
from .models import PictureModel
from .utils import upload_picture_to_azure
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def upload_picture(request):
    if request.method == 'POST' and request.FILES.get('picture'):
        picture = request.FILES['picture']
        # Upload picture to Azure Blob Storage
        picture_url = upload_picture_to_azure(picture)

        # e.g : mypic01.jpg -> mypic01
        name :str = request.FILES['picture'].name

        # Save metadata to the database     # TODO : uncomment the below and use them (instead of hard-coded values)
        # title = request.POST.get('title')
        # caption = request.POST.get('caption')
        # location = request.POST.get('location')

        title = name
        caption = f"Very Beautiful picture"
        location = "UK"

        PictureModel.objects.create(title=title, caption=caption, location=location, picture_url=picture_url)
        messages.success(request, 'Picture uploaded successfully!')
        return redirect('view_galleries')
    return render(request, 'upload_picture.html')

def view_galleries(request):
    pictures = PictureModel.objects.all()
    return render(request, 'view_galleries.html', {'pictures': pictures})


def home_view(request):
    return render(request, 'home.html')