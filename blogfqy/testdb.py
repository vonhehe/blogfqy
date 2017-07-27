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
#********添加数据**********
# def testdb(request):
#     test1 = Test(name='vonhehe')
#     test1.save()
#     return HttpResponse("<p>数据添加成功！~</p>")
#
# **********获取数据**********
def testdb(request):
    # 初始化
    response = ''
    response1 = ''

    #orm操作，通过objects这个模型管理器的all()获得所有行数据
    list = Test.objects.all() #相当于 select * from table

    #filter相当于sql中的where，设置条件过滤
    #response2 = Test.objects.filter(id=1)  #select * from table where id=1

    #获取单个对象
    #response3 = Test.objects.get(id=1)

    #限制返回的数据
    #Test.objects.order_by('name')[:2] # offset 0 limit 2

    #数据排序
    #Test.objects.order_by('id')

    #上面的方法可以连锁使用
    #Test.objects.filter(name='vonhehe').order_by('id')

    #输出所有数据
    for var in list:
        response1 += var.name +'</br>'
    response = response1
    return  HttpResponse('<h1>'+response+'</h1>')

#************更新数据**************
# def testdb(request):
#     #修改其中一个id=1的name字段，相当于SQL中的update
#     test1 = Test.objects.get(id=1)
#     test1.name = 'shasha'
#     test1.save()
#     # 另外一种方法
#     # Test.objects.filter(id=1).update(name= 'shasha')
#
#     #修改所有的列
#     #Test.objects.all().update(name = 'shasha')
#
#     return HttpResponse("<h1>修改成功！</h1>")
#------------删除数据------------
# def testdb(request):
#     test1 = Test.objects.get(id=3)
#     test1.delete()
#     #test1.save()
#
#     #删除一行数据
#     #Test.objects.filter(id=1).delete()
#
#     #删除所有数据
#     #Test.objects.all().delete()
#
#     return HttpResponse("<h>删除成功</h>")

