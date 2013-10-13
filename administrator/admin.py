# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *


class SuperAdmin(admin.ModelAdmin):
    """
    Super admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date') 
    # list_display = ('id', 'name')
    pass

admin.site.register(Super, SuperAdmin)

class InitialAdmin(admin.ModelAdmin):
    """
    Initial admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date') 
    # list_display = ('id', 'name')
    pass

admin.site.register(Initial, InitialAdmin)

class AssistAdmin(admin.ModelAdmin):
    """
    Assist admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date') 
    # list_display = ('id', 'name')
    pass

admin.site.register(Assist, AssistAdmin)

