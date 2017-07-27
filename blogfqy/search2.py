#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.11
@author: vonhehe
@contact: 615873982@qq.com
@software: PyCharm
@file: search2.py
@time: 2017/7/27 11:26
"""
from django.shortcuts import render
from django.views.decorators import csrf

def search_post(request):
    contxt = {}
    if request.POST:
        contxt['rlt'] = request.POST['q']

    return render(request,'post.html',contxt)