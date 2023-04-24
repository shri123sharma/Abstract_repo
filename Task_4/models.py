from django.db import models

# Create your models here.
class Blog(models.Model):
  
  title=models.CharField(max_length=255,null=True,blank=True)
  content=models.CharField(max_length=100,null=True,blank=True)

  def __str__(self):
    return self.title
