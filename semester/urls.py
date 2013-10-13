# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *  

urlpatterns = patterns('semester.views',
    url(r'form/semester/(?P<semester_id>\d+)/$', 'form_semester', name='semester_semester_form'),
    
    url(r'view/semester/(?P<semester_id>\d+)/$', 'view_semester', name='semester_semester_view'),
    
    url(r'list/semester/$', 'list_semester', name='semester_semester_list'),
    
    )
