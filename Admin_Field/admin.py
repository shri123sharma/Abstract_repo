from django.contrib import admin
from django.contrib import admin
from .models import *
# Register your models here.


admin.site.site_header = "DataFlair Django Tutorials"

class UserAdmin(admin.ModelAdmin):
  list_display=('id','name','age','email','phone_number','pin_code','address')
  list_display_links=('name',)
  change_list_template="admin/Admin_Field/change_form.html" 

admin.site.register(User,UserAdmin)

class PostAdmin(admin.ModelAdmin):
  list_display=('id','title','content','created_on','updated_on','comment_text')
  list_display_links=('id',)
admin.site.register(Post,PostAdmin)


