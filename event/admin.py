# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *


class EventAdmin(admin.ModelAdmin):
    """
    Event admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date')
    # list_display = ('id', 'name')
    pass

admin.site.register(Event, EventAdmin)

class MemberAdmin(admin.ModelAdmin):
    """
    Member admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date')
    # list_display = ('id', 'name')
    pass

admin.site.register(Member, MemberAdmin)
admin.site.register(TempEvent)
