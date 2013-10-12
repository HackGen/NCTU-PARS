from django.conf.urls import patterns, url

from reguser import views

urlpatterns = patterns('',
    url(r'^$', views.signup, name='signup'),
)
