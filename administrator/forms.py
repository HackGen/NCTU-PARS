# -*- coding: utf-8 -*-

from django import forms

from models import *


class SuperForm(forms.ModelForm):
    class Meta:
        model = Super


class InitialForm(forms.ModelForm):
    class Meta:
        model = Initial


class AssistForm(forms.ModelForm):
    class Meta:
        model = Assist



