# -*-coding:utf8 -*-

from __future__ import unicode_literals
from django.db import models

import time


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


# class Tb20161130(models.Model):
#     xuhao = models.CharField(max_length=8)
#     editor = models.CharField(max_length=50)
#     banming = models.CharField(max_length=16)
#     title = models.CharField(max_length=45)
#     imgsrc = models.CharField(max_length=80)
#     body = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'tb_2016_11_30'


class News(models.Model):
    id = models.IntegerField(primary_key=True)
    xuhao = models.CharField(max_length=8)
    editor = models.CharField(max_length=50)
    banming = models.CharField(max_length=16)
    title = models.CharField(max_length=45)
    imgsrc = models.CharField(max_length=80)
    body = models.TextField()

    def __str__(self):
        return self.banming

    class Meta:
        managed = False
        ordering = ['xuhao']
        # 自动获取当天的数据表
        db_table = 'tb_%s'%(time.strftime(u'%Y_%m_%d'))
