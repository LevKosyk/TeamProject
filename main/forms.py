<<<<<<< HEAD
from .models import Student
from django.forms import ModelForm, TextInput, NumberInput, ClearableFileInput

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'grade', 'photo']

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
            'photo': ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }
=======
from .models import Student
from django.forms import ModelForm, TextInput, NumberInput, ClearableFileInput

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'grade', 'photo']

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
            'photo': ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }
>>>>>>> 5984854642474ac2632e85ce90862a14376f31fe
