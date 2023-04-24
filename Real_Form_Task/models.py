from django.db import models

# Create your models here.
class User(models.Model):
  name=models.CharField(max_length=255,null=True,blank=True)
  age=models.IntegerField()
  email=models.EmailField(max_length=255,null=True, blank=True)

  def __str__(self):
    return self.name

class City(models.Model):
  city_name=models.CharField(max_length=255,null=True, blank=True)

  def __str__(self):
    return self.city_name

class Country(models.Model):
  country_name=models.CharField(max_length=100,null=True,blank=True)

  def __str__(self):
    return self.country_name