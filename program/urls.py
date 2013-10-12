# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *  

urlpatterns = patterns('program.views',
    url(r'form/program/(?P<program_id>\d+)/$', 'form_program', name='program_program_form'),
    
    url(r'view/program/(?P<program_id>\d+)/$', 'view_program', name='program_program_view'),
    
    url(r'list/program/$', 'list_program', name='program_program_list'),
    
    )
