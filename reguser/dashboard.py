from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def dashboard(request):
    #test event
    from event.models import TempEvent
    events = TempEvent.objects.order_by('start').reverse()
    return render_to_response('dashboard.html', {'events' : events}, context_instance=RequestContext(request))
