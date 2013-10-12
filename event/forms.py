# -*- coding: utf-8 -*-

from django import forms

from models import *


class EventForm(forms.ModelForm):
    class Meta:
        model = Event


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member



