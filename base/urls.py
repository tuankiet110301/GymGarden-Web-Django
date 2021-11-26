from django.http import HttpResponse
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^faq/$', views.faq, name='faq'),
    path('', views.homepage, name='home'),
    url(r'^home/$', views.homepage, name='home'),
]