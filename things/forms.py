"""Forms of the project."""
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your forms here.

class ThingForm(forms.Form):
    name = forms.CharField(label = "Name", max_length=36)
    description = forms.CharField(label = "Description")
    quantity = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)])
