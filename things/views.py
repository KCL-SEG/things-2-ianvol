from django.shortcuts import render
from .forms import SignUpForm

def home(request):
    form = SignUpForm()
    return render(request, 'home.html', {'form': form})
    

