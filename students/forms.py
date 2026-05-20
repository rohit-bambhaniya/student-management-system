from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    

    class Meta:

        model = Student

        fields = [
            'user',
            'student_name',
            'roll_num',
            'student_class',
            'phone',
            'address',
            'date_of_birth'
        ]

        widgets = {


            'student_name': forms.TextInput(attrs={
                'class':'form-control'
            }),

            'roll_num': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'student_class': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'address': forms.Textarea(attrs={
                'class': 'form-control'
            }),

            'date_of_birth': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'user': forms.Select(attrs={
                'class': 'form-control'
            }),
        }