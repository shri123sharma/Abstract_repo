from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import *
from django import forms

class UserForm(ModelForm):

  class Meta:
    model=User
    fields=['name','age','email']

  def clean(self):
    super(UserForm, self).clean()
    name = self.cleaned_data.get('name')
    email=self.cleaned_data.get('email')

    if name == None:
      raise ValidationError("Name Fields Is Required")

    if email == None:
      raise ValidationError("Email Fields Is Required")

    if User.objects.filter(email=email).exists():
      raise ValidationError("Email Already Exists")
    return self.cleaned_data

class CityForm(ModelForm):
  class Meta:
    model=City
    fields='__all__'

  def clean(self):
    super(CityForm, self).clean()
    city_name = self.cleaned_data.get('city_name')
  
    if city_name == None:
      raise ValidationError("CityName Fields Is Required")

class CountryForm(ModelForm):
  class Meta:
    model=Country
    fields='__all__'

  def clean(self):
    super(CountryForm, self).clean()
    country_name = self.cleaned_data.get('country_name')
    if country_name == None:
      raise ValidationError("CountryName Fields Is Required")