from django.db import models

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegSysForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True, help_text='A valid email address, please.')
    last_name = forms.CharField(label='Last name', required=True, max_length=30, help_text='30 characters max.')
    first_name = forms.CharField(label='First name', required=True, max_length=60, help_text='60 characters max.')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")    #order

    def save(self, commit=True):
        user = super(RegSysForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.last_name = self.cleaned_data['last_name']
        user.first_name = self.cleaned_data['first_name']
        if commit:
            user.save()
        return user
