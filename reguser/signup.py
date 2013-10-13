# -*- coding: utf-8 -*-
from django.db import models

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm
from reguser.models import RegUser

from django.contrib.auth.forms import ReadOnlyPasswordHashField

#class Department():

class RegForm(ModelForm):
    """
    A form that creates a user, with no privileges, from the given email.
    """
    class Meta:
        model = RegUser
        widgets = {
            #'username'  : forms.EmailInput(),
            'password'  : forms.PasswordInput(),
            'password1' : ReadOnlyPasswordHashField(),
            'password2' : forms.PasswordInput(),
            #'end_time'  : forms.SelectDateWidget(),
        }

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.username

    #def _html_output(...): pass

    def save(self, commit=True):
        user = super(RegSysForm, self).save(commit=False)

        #need to be random at first time
        user.set_password(self.cleaned_data["password1"])

        user.username = self.cleaned_data['username']
        #user.email = self.cleaned_data['username']

        #looking for better solution
        user.phone = self.cleaned_data['phone']
        user.last_name = self.cleaned_data['last_name']
        user.first_name = self.cleaned_data['first_name']
        user.is_nctu = self.cleaned_data['is_nctu']
        user.student_id = self.cleaned_data['student_id']
        user.end_time = self.cleaned_data['end_time']
        user.department = self.cleaned_data['department']

        if commit:
            user.save()
        return user
