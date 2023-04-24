from django import forms
from Multi_Form_Task_3.models import *

class StudentForm(forms.ModelForm):
  class Meta:
    model=StudentData
    fields='__all__'

class TeacherForm(forms.ModelForm):
  class Meta:
    models=TeacherData
    fields='__all__'

