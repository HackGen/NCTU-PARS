# -*- coding: utf-8 -*-

from django.forms import ModelForm

from models import Event, Member

from models import TempeEvent


class EventForm(ModelForm):
    class Meta:
        model = Event



class MemberForm(ModelForm):
    class Meta:
        model = Member


class TempEventForm(ModelForm):
    class Meta:
        model = TempEvent
