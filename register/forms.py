from django import forms
from django.forms import ModelForm, TextInput, EmailField, EmailInput
from .models import register, TRAINING_PURPOSE
from django.contrib import messages
# Create your models here.



class registerForm(forms.ModelForm):
    class Meta:
        model = register
        fields = (
            'name',
            'phone',
            'purpose',
        )
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Họ và tên'}),
            'phone': TextInput(attrs={'placeholder': 'Số điện thoại'}),
            'purpose': forms.Select(attrs={'placeholder': 'Mục tiêu tập luyện'}),
        }

