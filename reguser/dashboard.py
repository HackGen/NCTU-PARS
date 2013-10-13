from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def dashboard(request):
    return render_to_response('dashboard.html', context_instance=RequestContext(request))
