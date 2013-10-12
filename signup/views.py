# -*- coding:utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from signup.models import RegSysForm
from django import forms

def signup(request):
    if request.method == 'POST':
        form = RegSysForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = RegSysForm()

    for field in form.fields.keys():
        field_obj = form.fields[field]

        field_obj.widget.attrs = {
                'class' : 'form-control',
                'placeholder' : field_obj.help_text}
        field_obj.help_text = ''

    ##hide password field
    ##lopking for better solution
    #form.fields['password1'].widget = forms.HiddenInput()
    #form.fields['password2'].widget = forms.HiddenInput()

    return render_to_response('signup.html', {'form': form}, context_instance=RequestContext(request))
