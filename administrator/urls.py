# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *  

urlpatterns = patterns('administrator.views',
    url(r'form/super/(?P<super_id>\d+)/$', 'form_super', name='administrator_super_form'),
    
    url(r'view/super/(?P<super_id>\d+)/$', 'view_super', name='administrator_super_view'),
    
    url(r'list/super/$', 'list_super', name='administrator_super_list'),
    
    
    url(r'form/initial/(?P<initial_id>\d+)/$', 'form_initial', name='administrator_initial_form'),
    
    url(r'view/initial/(?P<initial_id>\d+)/$', 'view_initial', name='administrator_initial_view'),
    
    url(r'list/initial/$', 'list_initial', name='administrator_initial_list'),
    
    
    url(r'form/assist/(?P<assist_id>\d+)/$', 'form_assist', name='administrator_assist_form'),
    
    url(r'view/assist/(?P<assist_id>\d+)/$', 'view_assist', name='administrator_assist_view'),
    
    url(r'list/assist/$', 'list_assist', name='administrator_assist_list'),
    
    )
