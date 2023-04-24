from django import views
from . import views
from django.urls import path

urlpatterns = [
  
    path('multi_form/',views.MultiForm,name='multiform'),
]