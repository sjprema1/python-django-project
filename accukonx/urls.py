from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth

urlpatterns = [
    path('<int:id>', views.base, name='index'),
    path('home', views.home_page, name='index'),
    path('create/', views.create, name='create'),
    path('upload/',views.upload_file,name="upload")

]