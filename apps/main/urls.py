from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.index),
   url(r'^register$', views.register),
   url(r'^login$', views.login),
   url(r'^success$', views.success),
   url(r'^message/create$', views.create_message),
   url(r'^comment/create$', views.create_comment),
   url(r'^logout$', views.logout),
]