from django import forms
from .models import *

class carForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'model', 'year', 'price', 'category', 'description', 'image']


