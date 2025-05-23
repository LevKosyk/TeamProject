from .models import Student
from django.forms import ModelForm, TextInput, NumberInput


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'grade']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter name'
            }),
            'age': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter age'
            }),
            'grade': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter grade'
            }),
        }
