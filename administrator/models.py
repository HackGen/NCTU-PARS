# -*- coding: utf-8 -*-

from django.db import models


class Super(models.Model):


    user_id = models.ForeignKey('user.User', unique=True)



    @models.permalink
    def get_absolute_url(self):
        return ('administrator.views.view_super', [str(self.id)])



class Initial(models.Model):


    user_id = models.ForeignKey('user.User', unique=True)



    @models.permalink
    def get_absolute_url(self):
        return ('administrator.views.view_initial', [str(self.id)])



class Assist(models.Model):


    user_id = models.ForeignKey('user.User')
    semester_id = models.ForeignKey('semester.Semester')



    @models.permalink
    def get_absolute_url(self):
        return ('administrator.views.view_assist', [str(self.id)])




