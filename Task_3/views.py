from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib import messages
from .models import newslatteremail
 
def home(request):
    if 'subscribe' in request.POST:
        # import pdb;pdb.set_trace()
        email = newslatteremail()
        email.userEmail = request.POST.get("email")
        email.save()
        messages.info(
            request, 'You have successfully subscribed to our newslatter.')
     
    if 'unsubscribe' in request.POST:
        newslatteremail.objects.filter(
            userEmail=request.POST.get("email")).delete()
        messages.info(request, 'sorry to see you!!!')
         
    return render(request, 'news.html')
