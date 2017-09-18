#-*-coding:utf-8 -*-
from django.shortcuts import render, render_to_response, HttpResponseRedirect
#from django.http import HttpResponse
from blog.models import News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import time
from django.views.generic import ListView, DetailView
from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(label="email", max_length=100)
    pwd = forms.CharField(label="password", widget=forms.PasswordInput)
def login(request):
    if 'email' or 'pwd' not in request.GET:
        lf = LoginForm()
        return render_to_response("login.html", {"lf":lf})
    lf = LoginForm(request.GET)
    email = lf.data['email']
    pwd = lf.data['pwd']
    try:
        user = User.object.get(email=email)
    except User.DoesNotExist:
        pass
    else:
        if user.check_password(pwd):
            return HttpResponseRedirect("login in "+ user.email)
    return HttpResponseRedirect("/login")


class NewsListView(ListView):
    model = News
    template_name = "more.html"

class NewsDetailView(DetailView):
    model = News
    template_name = "detail.html"
# Create your views here.
class Varsto:
    '''
    储存变量
    '''
    time_today = time.strftime('%Y-%m-%d')

def start(request):
    #msg = Tb20170801.objects.filter().exclude(imgsrc='无配图').order_by('?')[:4]
    msg_nosrc = News.objects.filter().order_by('?')[:8]
    msg_src = News.objects.filter().exclude(imgsrc='无配图').order_by('?')[:4]
    #time_today = time.strftime('%Y-%m-%d')
    context = {
        'news': msg_src,   # 必定含有图片的新闻
        'msgs': msg_nosrc,  #  随机得到四条新闻,有没有图没关系
        'time_now': Varsto.time_today, #获取当天时间
    }
    return render(request, 'start.html', context)

def more(request):
    news_list = News.objects.all()
    paginator = Paginator(news_list, 10)  # 每页显示 10条新闻
    page = request.GET.get('page')
    #print(page)
    #print(type(page))   测试结果为 str
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        #raise Http404   #请求的页面不是整数，回复404
        news = paginator.page(1)
    except EmptyPage:
        # 如果用户请求的页码号超过了最大页码号，显示最后一页
        news = paginator.page(paginator.num_pages)

    context={
        'news': news,
        'time_now': Varsto.time_today
    }
    return render(request, 'more.html', context)


def home(request):
    # context = {}
    return render(request, 'home.html')

def love(request):
    #string = "桃之夭夭，灼灼其华。之子于归，宜其室家。桃之夭夭，有蕡其实。之子于归，宜其家室。桃之夭夭，其叶蓁蓁。之子于归，宜其家人"
    string = ["桃之夭夭 灼灼其华", "之子于归 宜其室家", "桃之夭夭 有蕡其实", "之子于归 宜其家室", "桃之夭夭 其叶蓁蓁", "之子于归 宜其家人"]
    return render(request, 'love.html', {'string': string})

def detail(request):
    news = News.objects.all()
    context={
        'news': news,
    }
    return render(request, 'detail.html', context)