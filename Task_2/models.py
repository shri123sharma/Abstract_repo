from django.db import models
# Create your models here.
from datetime import date
from django.db import models

class User(models.Model):
  name=models.CharField(max_length=100,null=True, blank=True)
  age=models.PositiveIntegerField(default=0)
  email=models.EmailField(max_length=255)
  

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    blog_objects=models.Manager()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    author_objects=models.Manager()

    def __str__(self):
        return self.name

class Entry(models.Model):
    user=models.ForeignKey(User,null=True, blank=True,on_delete=models.CASCADE,related_name='user')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,related_name='blog')
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    entry_objects=models.Manager()

    def __str__(self):
        return self.headline