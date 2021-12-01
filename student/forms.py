from django import forms
from django import forms
from student.models import student

class StudentForm(forms.ModelForm):
    class Meta:
        model=student
        fields="__all__"