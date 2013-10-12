# -*- coding: utf-8 -*-
from django.db import models

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.db.models.signals import post_save

#class Department():

class RegSysForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email.
    (modify from UserCreationForm)
    """

    #def __init__(self, *args, **kwargs):
    #    super (RegSysForm, self).__init__(*args,**kwargs)
    #    self.fields.pop('username')

    #username is email
    username = forms.EmailField(label='Email', required=True, help_text='請輸入有效的 Email。 A valid email address, please.')
    phone = forms.DecimalField(label='Phone', required=True, help_text='請輸入您的手機號碼。 Your phone number, please.')
    last_name = forms.CharField(label='Last name', required=True, max_length=30, help_text='30 characters max.')
    first_name = forms.CharField(label='First name', required=True, max_length=60, help_text='60 characters max.')

    is_nctu = forms.BooleanField(label='NCTU\'s student ?', required=False, help_text='')
    student_id = forms.DecimalField(label='Student ID', required=False, help_text='學號')
    end_time = forms.DateField(label='End Time', help_text='結束日期')

    department_choise = ( ('CS', 'CS'), )
    department = forms.CharField(widget=forms.Select(choices=department_choise))

    password1 = forms.CharField(widget=forms.PasswordInput(), required=False, help_text='請輸入密碼')
    password2 = forms.CharField(widget=forms.PasswordInput(), required=False, help_text='請再輸入密碼')

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.username

    #def _html_output(...): pass

    #class Meta:
    #    model = User
    #    fields = ('username', 'phone', 'last_name', 'first_name',)    #order

    def save(self, commit=True):
        user = super(RegSysForm, self).save(commit=False)

        #need to be random at first time
        user.set_password(self.cleaned_data["password1"])

        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['username']

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
