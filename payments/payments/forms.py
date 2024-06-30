from django import forms
from .models import Services, Subscription, ServiceUser

class CreateSubcriptionForm(forms.ModelForm): 
    class Meta: 
        model = Services
        fields = ['type', 'mode', 'company']


class SubscriptionForm(forms.ModelForm): 
    class Meta: 
        model = Subscription
        fields = ['user', 'service', 'amount']
    
    user = forms.ModelChoiceField(queryset=ServiceUser.objects.all(), empty_label="Select a user")
    service = forms.ModelChoiceField(queryset=Services.objects.all(), empty_label="Select a service")
    amount = forms.DecimalField(max_digits=7, decimal_places=2)
