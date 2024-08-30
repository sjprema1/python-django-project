from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

    path('register/', views.register),
    path('search_users/',views.SearchUser.as_view()),


]