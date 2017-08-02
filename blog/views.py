#-*-coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Tb20170801
import time
# Create your views here.

def start(request):
    #msg = Tb20170801.objects.filter().exclude(imgsrc='无配图').order_by('?')[:4]
    msg_nosrc = Tb20170801.objects.filter().order_by('?')[:8]
    msg_src = Tb20170801.objects.filter().exclude(imgsrc='无配图').order_by('?')[:4]
    time_today = time.strftime('%Y-%m-%d')
    context = {
        'news': msg_src,   # 含有图片的新闻
        'msgs': msg_nosrc,  #  随机得到四条新闻
        'time_now': time_today,
    }
    return  render(request, 'start.html', context)

def more(request):
    return render(request, 'more.html')

def home(request):
    # context = {}
    return render(request, 'home.html')

def love(request):
    return render(request, 'love.html')

# class Morenews:
#     '''
#     用于逐行展示更多新闻,用more.html 渲染
#     '''
#     template_name = 'more.html'
