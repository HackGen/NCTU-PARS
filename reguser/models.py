# -*- coding:utf-8 -*-
from django.db import models

from django.contrib.auth.models import UserManager
from django.db.models.signals import post_save

from django.contrib.auth.models import BaseUserManager

#from django.contrib.auth import get_user_model as user_model
#User = user_model()

from django.contrib.auth.models import AbstractBaseUser

from django.conf import settings

class RegUserManager(BaseUserManager):

    fields = ('RegUser', 'test')
    readonly_fields = ('password')

    def create_user(self, username, phone, password=None):
        """
        Creates and saves a User with the given email, phone, name.
        """

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username = self.normalize_email(username),
            phone = phone
        )

        passwd = make_random_password(length=10, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')
        user.set_password(passwd)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        u = self.create_user(username, password=password)
        u.is_admin = True
        u.save(using=self._db)
        return u

def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = RegUser.objects.get_or_create(user=instance)

#post_save.connect(create_user_profile, sender=RegUser)

class RegUser(AbstractBaseUser):

    list_filter = ('phone', 'student_id')

    #set label to form ?
    #set require ?

    #username is email
    #user = models.ForeignKey(User, unique=True, related_name='profile')

    #password1 = models.CharField(max_length=30, help_text='請輸入密碼')
    #password2 = models.CharField(max_length=30, help_text='請再輸入密碼')

    phone       = models.DecimalField(max_digits=20, decimal_places=10, help_text='請輸入您的手機號碼 Your phone number, please.')
    is_nctu     = models.BooleanField(help_text='')
    student_id  = models.DecimalField(max_digits=20, decimal_places=10, help_text='學號')
    end_time    = models.DateField(help_text='結束日期')

    department_choise = ( ('CS', 'CS'), )
    department = models.CharField(max_length=30, choices=department_choise)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone']



    #important
    objects = RegUserManager()


    def __str__(self):
        return "%s's profile" % self.user
