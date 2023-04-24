from django.shortcuts import render
from django import forms
from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import *
from .import forms

# Create your views here.
# blog/views.py

# @login_required
# def edit_blog(request, blog_id):
#    blog = get_object_or_404(Blog, id=blog_id)
#    edit_form = forms.BlogForm(instance=blog)
#    delete_form = forms.DeleteBlogForm()
#    if request.method == 'POST':
#        pass
#    context = {
#        'edit_form': edit_form,
#        'delete_form': delete_form,
#    }
#    return render(request, 'blog/edit_blog.html', context=context)

@login_required
def edit_blog(request, blog_id):
    # import pdb;pdb.set_trace()
    blog = get_object_or_404(Blog, id=blog_id)
    edit_form = forms.BlogForm(instance=blog)
    delete_form = forms.DeleteBlogForm()
    if request.method == 'POST':
        if 'edit_blog' in request.POST:
            edit_form = forms.BlogForm(request.POST, instance=blog)
            if edit_form.is_valid():
                edit_form.save()
                return HttpResponse("edit_blog")
        if 'delete_blog' in request.POST:
            delete_form = forms.DeleteBlogForm(request.POST)
            if delete_form.is_valid():
                blog.delete()
                return HttpResponse("delete_blog")
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
    }
    return render(request, 'blog/edit_blog.html', context=context)
