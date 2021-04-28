from django import forms
from nariApp.models import Student 

class StudentsRegistry(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
