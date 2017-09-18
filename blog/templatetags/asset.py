#!/usr/bin/env python
#-*- encoding: utf-8 -*-
"""
@version:python3.5 &&
@software:PyCharm
@file:asset.py
@author:vonhehe
@contact:vonhehe@gmail.com
@time:2017/9/18 10:30
"""
from django import template
from blogfqy.settings import DEBUG
register = template.Library()

@register.filter
def asset(value):
    if  not DEBUG:
        return "/static/css/" +value
    return "/static/style.css"

#不同的设置加载不同的css等的过滤器
