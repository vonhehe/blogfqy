#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.11
@author: vonhehe
@contact: 615873982@qq.com
@software: PyCharm
@file: search.py
@time: 2017/7/27 10:26
"""
from django.http import HttpResponse
from django.shortcuts import render_to_response

#表单
def search_form(request):

    return render_to_response('search_form.html')

def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message ='你搜索的内容是'+request.GET['q']
    else:
        message = '你提交了空表单'

    return HttpResponse(message)
