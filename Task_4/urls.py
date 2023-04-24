# fotoblog/urls.py
from django import views
from . import views
from django.urls import path

urlpatterns = [

    path('blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
]