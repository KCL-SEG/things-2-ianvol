"""Forms of the project."""
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your forms here.

class ThingForm(forms.Form):
    name = forms.CharField(label = "Name", max_length=35)
    description = forms.CharField(label='description', max_length=120, widget=forms.Textarea)
    quantity = forms.IntegerField(label="Quantity", validators=[MinValueValidator(0), MaxValueValidator(50)])
