from django.shortcuts import render, redirect
from .forms import registerForm
from .models import register
from django import forms
from django.contrib import messages
import datetime
# Create your views here.



def registerFormation(request):
    templates_name = 'goitap.html'
    form = registerForm()
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            print('Save')
            print(datetime.datetime.now())
            print(form)
            form.save()
    else:
        form = registerForm()
    return render(request, templates_name, {'form': form})







