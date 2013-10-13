# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import get_object_or_404

from models import *
from forms import *



def view_semester(request, semester_id):
    """
    Allow input of data on semester
    """
    semester = get_object_or_404(Semester, pk=semester_id)
    context = {'semester': semester }
    return render_to_response('semester_view.html',
                              context,
                              context_instance=RequestContext(request))



def list_semester(request):
    """
    Display a list of Semester paginated
    """
    semester_list = Semester.objects.all()
    paginator = Paginator(semester_list, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        semester_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        semester_list = paginator.page(paginator.num_pages)

    context = {'semester_list': semester_list }
    return render_to_response('semester_list.html',
                              context,
                              context_instance=RequestContext(request))


def form_semester(request, semester_id):
    """
    Allow input of data on semester
    """
    semester = get_object_or_404(Semester ,pk=semester_id)
    if request.method == "POST":
        form = SemesterForm(request.POST, instance=semester)
        if form.is_valid():
            form.save()
    else:
        form = SemesterForm(instance=semester)

    context = {'semester': semester,
               'semester_form': form }

    return render_to_response('semester_form.html',
                              context,
                              context_instance=RequestContext(request))



