from django.contrib import admin
from custom_admin.models import *
# Register your models here.

class UserInline(admin.StackedInline):
  model=User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','age','email']
    change_form_template="admin/custom_admin/change_form.html"
  
class ProductInline(admin.StackedInline):
  model=Product

class OrderItemInline(admin.StackedInline):
    model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'created']
    change_list_template="admin/custom_admin/change_list.html"
    inlines = [OrderItemInline]
    fieldsets=[('user_detail',{'fields':['user']}),]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'count']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['title', 'price']
    fieldsets=[('Title',{'fields':['title']}),('Price',{'fields':['price']})]
  

    

