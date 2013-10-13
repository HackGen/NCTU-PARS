# stole from http://stackoverflow.com/questions/8456714/django-password-reset-email-subject
from django.contrib.auth.views import password_reset as django_password_reset
from django.contrib.auth.forms import PasswordResetForm

# reuse Django view, but change form
def password_reset(*args, **kwargs):
    kwargs['post_reset_redirect'] = '/'
    kwargs['from_email'] = 'noreply'
    return django_password_reset(*args, **kwargs)
