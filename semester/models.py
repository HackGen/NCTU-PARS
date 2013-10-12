from django.db import models
from program.models import Program

class Semester(models.Model):
    program_id = models.ForeignKey('Program')
    year = models.IntegerField(default = date.today().year)
    season = 


