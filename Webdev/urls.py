"""Webdev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from article.views import blog, reslug
from base.views import faq

urlpatterns = [
    url(r'^$', include('base.urls')),
    path('summernote/', include('django_summernote.urls')),
    url(r'^home/$', include('base.urls')),
    url(r'^goitap/$', include('register.urls')),
    url(r'^blog/$', blog, name='blog'),
    path('admin/', admin.site.urls),
    url(r'^blog/(?P<slug>[\w-]+)/$', reslug, name='reslug'),
    url(r'^faq/$', faq),
]

if settings.DEBUG:
    urlpatterns += + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)