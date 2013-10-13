# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import get_object_or_404

from models import *
from forms import *



def view_super(request, super_id):
    """
    Allow input of data on super
    """
    super = get_object_or_404(Super, pk=super_id)
    context = {'super': super }
    return render_to_response('super_view.html',
                              context,
                              context_instance=RequestContext(request))



def list_super(request):
    """
    Display a list of Super paginated
    """
    super_list = Super.objects.all()
    paginator = Paginator(super_list, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        super_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        super_list = paginator.page(paginator.num_pages)

    context = {'super_list': super_list }
    return render_to_response('super_list.html',
                              context,
                              context_instance=RequestContext(request))


def form_super(request, super_id):
    """
    Allow input of data on super
    """
    super = get_object_or_404(Super ,pk=super_id)
    if request.method == "POST":
        form = SuperForm(request.POST, instance=super)
        if form.is_valid():
            form.save()
    else:
        form = SuperForm(instance=super)

    context = {'super': super,
               'super_form': form }

    return render_to_response('super_form.html',
                              context,
                              context_instance=RequestContext(request))




def view_initial(request, initial_id):
    """
    Allow input of data on initial
    """
    initial = get_object_or_404(Initial, pk=initial_id)
    context = {'initial': initial }
    return render_to_response('initial_view.html',
                              context,
                              context_instance=RequestContext(request))



def list_initial(request):
    """
    Display a list of Initial paginated
    """
    initial_list = Initial.objects.all()
    paginator = Paginator(initial_list, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        initial_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        initial_list = paginator.page(paginator.num_pages)

    context = {'initial_list': initial_list }
    return render_to_response('initial_list.html',
                              context,
                              context_instance=RequestContext(request))


def form_initial(request, initial_id):
    """
    Allow input of data on initial
    """
    initial = get_object_or_404(Initial ,pk=initial_id)
    if request.method == "POST":
        form = InitialForm(request.POST, instance=initial)
        if form.is_valid():
            form.save()
    else:
        form = InitialForm(instance=initial)

    context = {'initial': initial,
               'initial_form': form }

    return render_to_response('initial_form.html',
                              context,
                              context_instance=RequestContext(request))




def view_assist(request, assist_id):
    """
    Allow input of data on assist
    """
    assist = get_object_or_404(Assist, pk=assist_id)
    context = {'assist': assist }
    return render_to_response('assist_view.html',
                              context,
                              context_instance=RequestContext(request))



def list_assist(request):
    """
    Display a list of Assist paginated
    """
    assist_list = Assist.objects.all()
    paginator = Paginator(assist_list, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        assist_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        assist_list = paginator.page(paginator.num_pages)

    context = {'assist_list': assist_list }
    return render_to_response('assist_list.html',
                              context,
                              context_instance=RequestContext(request))


def form_assist(request, assist_id):
    """
    Allow input of data on assist
    """
    assist = get_object_or_404(Assist ,pk=assist_id)
    if request.method == "POST":
        form = AssistForm(request.POST, instance=assist)
        if form.is_valid():
            form.save()
    else:
        form = AssistForm(instance=assist)

    context = {'assist': assist,
               'assist_form': form }

    return render_to_response('assist_form.html',
                              context,
                              context_instance=RequestContext(request))



