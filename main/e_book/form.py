from django import forms
from .models import Book_details

class YourForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'ckeditor'}))
    class Meta:
        model=Book_details
        fields=('content',)
