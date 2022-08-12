from dataclasses import field
from django import forms
from myapp.models import Student

# Create your models here.
class StudentForms(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__" 
        
        