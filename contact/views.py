# -*- coding:utf-8 -*-

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail

from django import forms
from contact.models import *

#def form(request):
#    form = ContactForm(request.POST)
#    return

def process_Contact(request):
    if request.method == 'POST':
        if True or form.is_valid():
            mail_sub = u"[PARS] {}".format(request.POST['subject'])
            mail_msg = u"User {} {} from {} said:\n  {}".format(
                                               request.POST['first_name'],
                                               request.POST['last_name'],
                                               request.POST['email'],
                                               request.POST['message'])

            # XXX: use my mailbox for testing
            send_mail(mail_sub, mail_msg, 'contact@pars.nctucs.net',
                ['xatierlike@gmail.com'], fail_silently=False)
            return HttpResponseRedirect("/")
    else:
        pass

    return render_to_response('contact.html', context_instance=RequestContext(request))
