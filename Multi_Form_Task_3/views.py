from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import StudentForm,TeacherForm
from django.views.generic.list import ListView
from django.urls import reverse
from django.views.generic.edit import FormView

# Create your views here.

class SchoolData(FormView):
   form_classes = {
      'student_form' : StudentForm,
      'teacher_form' : TeacherForm,
   }
   template_name = 'home.html'

   def get_success_url(self):
      return reverse('home')

   def forms_valid(self, forms):
      student = forms['student_form'].save(commit=False)
      teacher=forms['teacher_form'].save(commit=False)
      return super(SchoolData, self).forms_valid(forms)
