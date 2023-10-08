"""Forms of the project."""
from django import forms
# Create your forms here.

class SignUpForm(forms.Form):
    name = forms.CharField(label = "Name")
    description = forms.CharField(label = "Description")
    quantity = forms.IntegerField(label = "Quantity")
