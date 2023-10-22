from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
from .models import User,Profile

class SignupForm(UserCreationForm):
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields=('email','password1','password2')

class Signin_Form(forms.Form):
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

class Profile_Form(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control m-1'}))
    addess=forms.CharField(label='Address',widget=forms.Textarea(attrs={'class':'form-control m-1'}) )

class Passchangeform(PasswordChangeForm):
    model =User
    old_password=forms.CharField(label='Old password ', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1=forms.CharField(label='New password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(label='Confirm new password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
