# -*- coding:utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from reguser.signup import RegForm
from django import forms


from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def signup(request):

    #print to string
    u = "%s" % request.user

    if u != 'AnonymousUser':
        return HttpResponseRedirect("/dashboard")

    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = RegForm()

    #form.fields['username'].help_text = 'foo'
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

def RegLogin(request):

    #print to string
    u = "%s" % request.user

    if u != 'AnonymousUser':
        return HttpResponseRedirect("/dashboard")

    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/dashboard')
        else:
            return HttpResponseRedirect('/signup')
    return render_to_response('index.html', {'user': request.user}, context_instance=RequestContext(request))

def RegLogout(request):
    try:
        logout(request)
    except:
        pass
    return HttpResponseRedirect('/')
