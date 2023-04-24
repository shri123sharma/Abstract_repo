from django.db import models

# Create your models here.
from django.db import models
 
# creating database model to store email
class newslatteremail(models.Model):
    userEmail = models.EmailField(max_length=254)
 
    def __str__(self):
        return self.userEmail