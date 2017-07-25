#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.11
@author: vonhehe
@contact: 615873982@qq.com
@software: PyCharm
@file: testdb.py
@time: 2017/7/25 16:43
"""
from django.http import HttpResponse
from blog.models import Test
#数据库操作
def testdb(request):
    test1 = Test(name='vonhehe')
    test1.save()
    return HttpResponse("<p>数据添加成功！~</p>")