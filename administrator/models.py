from django.db import models
from reguser.models import RegUser
from semester.models import Semester

class SuperAdmin(models.Model):
    reguser_id = models.ForeignKey('RegUser')

class InitialAdmin(models.Model):
    reguser_id = models.ForeignKey('RegUser')

class Assistant(models.Model):
    reguser_id = models.ForeignKey('RegUser')
    semester_id = models.ForeignKey('Semester')

