from django import forms
from .models import Services

class SubcriptionForm(forms.ModelForm): 
    class Meta: 
        model = Services
        fields = ['user', 'service', 'amount']