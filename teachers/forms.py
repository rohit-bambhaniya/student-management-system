from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):

    class Meta:

        model = Teacher

        fields = [
            'user',
            'teacher_name',
            'subject',
            'qualifications',
            'experience',
            'phone',
            'address',
            'salary',
            'joining_date'

        ]

        widgets = {

            'teacher_name' : forms.TextInput(attrs={
                'class':'form-control'
               
            }),

            'subject':forms.TextInput(attrs={
                'class':'form-control'
                
            }),

            'qualifications':forms.TextInput(attrs={
                'class':'form-control'
                
            }),

            'experience':forms.NumberInput(attrs={
                'class':'form-control'

            }),

            'phone':forms.TextInput(attrs={
                'class':'form-control'

            }),

            'address':forms.Textarea(attrs={
                'class':'form-control'

            }),

            'salary':forms.TextInput(attrs={
                'class':'form-control'

            }),

            'joining_date':forms.DateInput(attrs={
                'class':'form-control',
                'type': 'date'
            }),

            
            'user': forms.Select(attrs={
                'class': 'form-control'
                
            }),

        }
