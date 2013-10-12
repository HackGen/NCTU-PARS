# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import get_object_or_404

from models import *
from forms import *



def view_event(request, event_id):
    """
    Allow input of data on event
    """
    event = get_object_or_404(Event, pk=event_id)
    context = {'event': event }
    return render_to_response('event_view.html',
                              context,
                              context_instance=RequestContext(request))



def list_event(request):
    """
    Display a list of Event paginated
    """
    event_list = Event.objects.all()
    paginator = Paginator(event_list, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        event_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        event_list = paginator.page(paginator.num_pages)

    context = {'event_list': event_list }
    return render_to_response('event_list.html',
                              context,
                              context_instance=RequestContext(request))


def form_event(request, event_id):
    """
    Allow input of data on event
    """
    event = get_object_or_404(Event ,pk=event_id)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
    else:
        form = EventForm(instance=event)

    context = {'event': event,
               'event_form': form }

    return render_to_response('event_form.html',
                              context,
                              context_instance=RequestContext(request))
        



def view_member(request, member_id):
    """
    Allow input of data on member
    """
    member = get_object_or_404(Member, pk=member_id)
    context = {'member': member }
    return render_to_response('member_view.html',
                              context,
                              context_instance=RequestContext(request))



def list_member(request):
    """
    Display a list of Member paginated
    """
    member_list = Member.objects.all()
    paginator = Paginator(member_list, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        member_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        member_list = paginator.page(paginator.num_pages)

    context = {'member_list': member_list }
    return render_to_response('member_list.html',
                              context,
                              context_instance=RequestContext(request))


def form_member(request, member_id):
    """
    Allow input of data on member
    """
    member = get_object_or_404(Member ,pk=member_id)
    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
    else:
        form = MemberForm(instance=member)

    context = {'member': member,
               'member_form': form }

    return render_to_response('member_form.html',
                              context,
                              context_instance=RequestContext(request))
        


