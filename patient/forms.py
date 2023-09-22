from django import forms
from .models import Patient
from django.forms import ModelForm

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['patient_num','first_name','last_name','birthday', 'latest_diagnosis']
        widgets = {
            'latest_diagnosis': forms.DateInput(attrs={'type': 'date'}),
            'birthday': forms.DateInput(attrs={'type': 'date'}),

        }
         