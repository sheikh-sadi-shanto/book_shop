from django import forms
from .models import BillingAdress

class Address(forms.ModelForm):
    name=forms.CharField( widget=forms.TextInput(attrs={'class':'form-control'}))
    number=forms.CharField( widget=forms.TextInput(attrs={'class':'form-control'}))
    distric=forms.CharField(label='District', widget=forms.TextInput(attrs={'class':'form-control'}))
    address=forms.CharField( widget=forms.Textarea(attrs={'class':'form-control','rows':'5'}))
    class Meta:
        model = BillingAdress
        exclude=('user',)
