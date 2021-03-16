from django import forms

from .models import Job
from .models import Application

class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 
        'short_description', 
        'long_description', 
        'company_name', 
        'company_address', 
        'company_city', 
        'company_country', 
        'company_amount'
        ]

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['content', 'experience']