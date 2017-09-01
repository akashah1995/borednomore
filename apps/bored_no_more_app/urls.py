from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.intro),
    url(r'home$', views.index),
    url(r'getcategory$', views.getcategory),
    url(r'register$', views.register),
    url(r'login$', views.login),
    url(r'getpage$', views.getpage),
    url(r'test$', views.test),
    url(r'addEvent$', views.addEvent),
    url(r'userEvents$', views.userEvents),
    url(r'deleteEvent/(?P<variable>\d+)$', views.deleteEvent),
    url(r'logout$', views.logout)

]