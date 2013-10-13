# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *


class ProgramAdmin(admin.ModelAdmin):
    """
    Program admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date') 
    # list_display = ('id', 'name')
    pass

admin.site.register(Program, ProgramAdmin)

