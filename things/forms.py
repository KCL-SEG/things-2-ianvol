"""Forms of the project."""
from django import forms
from .models import Thing
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your forms here.

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
