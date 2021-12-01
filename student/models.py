from django.db import models
from django.forms import ModelForm, Textarea


# Create your models here.
class student(models.Model):
    student_no=models.IntegerField()
    student_name=models.CharField(max_length=30)
    student_DOB=models.DateField(null=True, blank=True)
    student_DOJ=models.DateField(null=True, blank=True)
    class meta:
        db_table="student"