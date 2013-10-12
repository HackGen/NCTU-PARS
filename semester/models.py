# -*- coding: utf-8 -*-

from django.db import models


class Semester(models.Model):
    
    
    program_id = models.ForeignKey('program.Program')
    year = models.IntegerField(default="lambda: daetime.date.today().year")
    season = models.CharField(choices=(("Spring","Spring"),("Summer","Summer"),("Fall","Fall"),("Winter","Winter")), max_length=10)
    place = models.CharField(null=True, blank=True, max_length=50)
    info = models.TextField(null=True, blank=True)
    


    @models.permalink
    def get_absolute_url(self):
        return ('semester.views.view_semester', [str(self.id)])



    def __unicode__(self):
        return self.season

    def __unicode__(self):
        return self.place


