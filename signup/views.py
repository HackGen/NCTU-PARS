from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from signup.models import RegSysForm

def signup(request):
    if request.method == 'POST':
        form = RegSysForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = RegSysForm()

    form.fields['username'].widget.attrs['class'] = 'form-control'
    form.fields['password1'].widget.attrs['class'] = 'form-control'
    form.fields['password2'].widget.attrs['class'] = 'form-control'
    form.fields['email'].widget.attrs['class'] = 'form-control'
    form.fields['last_name'].widget.attrs['class'] = 'form-control'
    form.fields['first_name'].widget.attrs['class'] = 'form-control'

    return render_to_response('signup.html', {'form': form}, context_instance=RequestContext(request))
