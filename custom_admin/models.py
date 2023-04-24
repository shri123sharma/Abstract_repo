from django.db import models
# from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
  name=models.CharField(max_length=255,null=True,blank=True)
  age=models.IntegerField()
  email=models.EmailField(max_length=255,null=True, blank=True)

  def __str__(self):
    return self.name

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.created.date()}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product}_{self.count}"
