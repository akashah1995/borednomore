from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.intro),
    url(r'home$', views.index),
    url(r'getcategory$', views.getcategory),
    url(r'register$', views.register),
    url(r'login$', views.login),
    url(r'getpage$', views.getpage)
]