# -*- coding: utf-8 -*-

from django import forms

from models import *


class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester



