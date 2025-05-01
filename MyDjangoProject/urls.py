from django.contrib import admin
from django.urls import path, include
from pictures_app import views as pictures_app_views


urlpatterns = [
    # path('', pictures_app_views.home_view, name='home'),
    path("", pictures_app_views.view_galleries, name="home"),
    path("admin/", admin.site.urls),
    path("pictures/", include("pictures_app.urls")),
    path("users/", include("users_app.urls")),
]
