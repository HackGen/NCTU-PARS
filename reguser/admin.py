from django.contrib import admin
from reguser.models import *

admin.site.register(RegUser, RegUserManager)
