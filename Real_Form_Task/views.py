from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
# Create your views here.

def MultiForm(request):
  if request.method=="POST":
    user_form=UserForm(request.POST,request.FILES)
    city_form=CityForm(request.POST,request.FILES)
    country_form=CountryForm(request.POST,request.FILES)
    if all([user_form.is_valid(), city_form.is_valid(), country_form.is_valid()]):
      user_form_save=user_form.save()
      city_form_save=city_form.save(commit=False)
      city_form_save.user_form_save=user_form_save
      city_form_save.save()
      country_form_save=country_form.save(commit=False)
      country_form_save.user_form_save=user_form_save
      country_form_save.save()
      return HttpResponse("data submitted successfully")
  else:
      user_form = UserForm()
      city_form=CityForm()
      country_form=CountryForm()
  return render(request, 'multi_form.html',{'user_form': user_form, 'city_form': city_form, 'country_form': country_form})

  


