from django.http import HttpResponse
from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', views.reslug, name="reslug"),
    url(r'^$', views.blog, name="blog"),
]