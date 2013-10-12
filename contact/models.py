#-*- coding:utf-8 -*-
from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email_address = models.EmailField()
    subject = models.CharField(max_length=50)
    content = models.TextField()
    send_date = models.DateTimeField('date of the mail be sent')

