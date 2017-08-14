#! /usr/bin/env python
# -*- encoding:utf-8 -*-
# @Filename:urls
# @Time : 2017/8/2-22:43
# @Author: Vonhehe

from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^start.html/', views.start, name='start'),
    url(r'^love.html/', views.love, name='love'),
#    url(r'^more/(?P<page>[0-9]+)/$', views.more, name='more'),
    url(r'^more/', views.more, name='more'),
]