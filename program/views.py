# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import get_object_or_404

from models import *
from forms import *



def view_program(request, program_id):
    """
    Allow input of data on program
    """
    program = get_object_or_404(Program, pk=program_id)
    context = {'program': program }
    return render_to_response('program_view.html',
                              context,
                              context_instance=RequestContext(request))



def list_program(request):
    """
    Display a list of Program paginated
    """
    program_list = Program.objects.all()
    paginator = Paginator(program_list, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        program_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        program_list = paginator.page(paginator.num_pages)

    context = {'program_list': program_list }
    return render_to_response('program_list.html',
                              context,
                              context_instance=RequestContext(request))


def form_program(request, program_id):
    """
    Allow input of data on program
    """
    program = get_object_or_404(Program ,pk=program_id)
    if request.method == "POST":
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
    else:
        form = ProgramForm(instance=program)

    context = {'program': program,
               'program_form': form }

    return render_to_response('program_form.html',
                              context,
                              context_instance=RequestContext(request))



