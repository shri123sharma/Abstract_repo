from django.contrib import admin
from .models import *

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
  list_display=['name','tagline']
admin.site.register(Blog,BlogAdmin)


class AuthorAdmin(admin.ModelAdmin):
  list_display=['name','email']
admin.site.register(Author,AuthorAdmin)

class EntryAdmin(admin.ModelAdmin):
  list_display=['headline','body_text','pub_date','mod_date','number_of_comments','number_of_pingbacks','rating']
admin.site.register(Entry,EntryAdmin)
