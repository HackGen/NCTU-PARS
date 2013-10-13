# -*- coding: utf-8 -*-

from django.db import models


class Program(models.Model):


    initial_admin_id = models.ForeignKey('administrator.Initial')
    title = models.CharField(max_length=50)
    intro = models.TextField(null=True, blank=True)



    @models.permalink
    def get_absolute_url(self):
        return ('program.views.view_program', [str(self.id)])



    def __unicode__(self):
        return self.title


