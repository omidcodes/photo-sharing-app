from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_picture, name='upload_picture'),
    path('pictures/', views.view_pictures, name='view_pictures'),
]