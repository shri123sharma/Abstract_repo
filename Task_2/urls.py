from django import views
from . import views
from django.urls import path

urlpatterns = [
    path('custom/',views.my_custom_sql,name='multiform'),
]