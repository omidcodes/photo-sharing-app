from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.upload_picture, name="upload_picture"),
    path("gallery/", views.view_galleries, name="view_galleries"),
]
