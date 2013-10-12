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

def parm_is_valid(post):
    # check all post parameters are valid
    if post['subject'] not in ["General", "Contest_issues", "Suggestions"]:
        return False
    elif not post['first_name']:
        return False
    elif not post['last_name']:
        return False
    elif not post['message'] :
        return False

    # django builtin mail validator
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(post['email'])
    except ValidationError:
        return False

    return True


def process_Contact(request):
    err = False
    if request.method == 'POST':
        if parm_is_valid(request.POST):
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
            err = True


    ci=RequestContext(request)
    ci['error'] = err
    ci['first_name'] = request.POST.get('first_name', '')
    ci['last_name'] = request.POST.get('last_name', '')
    ci['email'] = request.POST.get('email', '')
    ci['message'] = request.POST.get('message', '')
    return render_to_response('contact.html', context_instance=ci)
