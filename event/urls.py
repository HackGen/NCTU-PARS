# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *  

urlpatterns = patterns('event.views',
    url(r'form/event/(?P<event_id>\d+)/$', 'form_event', name='event_event_form'),
    
    url(r'view/event/(?P<event_id>\d+)/$', 'view_event', name='event_event_view'),
    
    url(r'list/event/$', 'list_event', name='event_event_list'),
    
    
    url(r'form/member/(?P<member_id>\d+)/$', 'form_member', name='event_member_form'),
    
    url(r'view/member/(?P<member_id>\d+)/$', 'view_member', name='event_member_view'),
    
    url(r'list/member/$', 'list_member', name='event_member_list'),
    
    )
