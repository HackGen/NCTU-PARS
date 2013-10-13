# -*- coding: utf-8 -*-

from django.db import models


class Event(models.Model):


    semester_id = models.ForeignKey('semester.Semester')
    title = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    info = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    signup_start = models.DateTimeField()
    signup_end = models.DateTimeField()
    max_attendees = models.IntegerField()



    @models.permalink
    def get_absolute_url(self):
        return ('event.views.view_event', [str(self.id)])



    def __unicode__(self):
        return self.title

    def __unicode__(self):
        return self.place

    class Meta:
        app_label="events"

class Member(models.Model):


    user_id = models.ForeignKey('user.User')
    event_id = models.ForeignKey('event.Event')
    score = models.IntegerField(null=True, blank=True)



    @models.permalink
    def get_absolute_url(self):
        return ('event.views.view_member', [str(self.id)])


    class Meta:
        app_label="members"

class TempEvent(models.Model):
    #no user

    title = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    info = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    signup_start = models.DateTimeField()
    signup_end = models.DateTimeField()
    max_attendees = models.IntegerField()

    def __unicode__(self):
        return self.title
