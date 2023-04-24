from django.db import models
from django import forms
from django.core.exceptions import ValidationError

# Create your models here.
def validate_user_field(value):
  if len(value) <= 5:
      raise ValidationError("if name characters in more then 5 characters")     
  else:
    return value

def validate_phone_number(value):
  if value<10 or value>10:
    raise ValidationError('Please correct phone number')
  else:
    return value
def validate_pin_code(value):
  if value<6 or value>6:
    raise ValidationError('Only 6 digits pin code are allowed')

class User(models.Model):
  name=models.CharField(max_length=255,null=True,blank=True,validators =[validate_user_field])
  age=models.PositiveIntegerField()
  email=models.EmailField(max_length=255,unique=True,error_messages ={
                    "unique":"The Geeks Field you entered is not unique."
                    })
  phone_number=models.PositiveIntegerField(validators=[validate_phone_number])
  address=models.CharField(max_length=255,help_text='please fill in address')
  pin_code=models.IntegerField(default=743847,validators=[validate_pin_code])

  def __str__(self):
    return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, 
        related_name="blog_posts",
        )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)
    summary = models.CharField(max_length=500, null=True, blank=True)
    comment_text=models.TextField(max_length=650,blank=True,null=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
      return self.title

    
