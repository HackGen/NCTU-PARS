# -*- coding: utf-8 -*-

from django import forms

from models import *


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program



