from django import forms
from .models import Students,Classroom


class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields =['name']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['classroom', 'register_no', 'name', 'attendance']