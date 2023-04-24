from django.urls import path,include
from . import views
urlpatterns = [
   path('school/',views.SchoolData.as_view(),name='home'),
]