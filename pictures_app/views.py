from django.shortcuts import render, redirect
from .models import PictureModel
from .utils import upload_picture_to_azure
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

@login_required
def upload_picture(request):
    if request.method == 'POST' and request.FILES['picture']:
        picture = request.FILES['picture']
        # Upload picture to Azure Blob Storage
        picture_url = upload_picture_to_azure(picture)

        # Save metadata to the database
        title = request.POST.get('title')
        caption = request.POST.get('caption')
        location = request.POST.get('location')

        PictureModel.objects.create(title=title, caption=caption, location=location, picture_url=picture_url)
        return HttpResponse('Picture uploaded successfully!')
    return render(request, 'upload_picture.html')

def view_pictures(request):
    pictures = PictureModel.objects.all()
    return render(request, 'view_pictures.html', {'pictures': pictures})


def home_view(request):
    return render(request, 'home.html')  # make sure you have a template called home.html