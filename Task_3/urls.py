from django.urls import path
from . import views
 
urlpatterns = [
    
    # URL to open home page
    path("home/", views.home, name='home'),
]