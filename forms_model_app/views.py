from django.shortcuts import render
from . import forms
# Create your views here.


def home(request):
    form = forms.DetailForm()
    return render(request, 'home.html', {'form': form})
