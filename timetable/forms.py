from django import forms
from .models import time_table
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class time_table_form(forms.ModelForm):
    class Meta:
        model = time_table
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        fields=['username','email,''password1','password1']
