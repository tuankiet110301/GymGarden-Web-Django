from django.http import HttpResponse
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.registerFormation, name='registerFormation'),
    url(r'^goitap/$', views.registerFormation, name='registerFormation'),
]