from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Tb20170801
# Create your views here.
def index(request):
    #msg = Tb20170801.objects.filter().exclude(imgsrc='无配图').order_by('?')[:4]
    msg1 = Tb20170801.objects.filter().order_by('?')[:8]
    msg = Tb20170801.objects.filter().exclude(imgsrc='无配图').order_by('?')[:4]
    #print(msg1)
    context = {
        'news':msg,   # 含有图片的新闻
        'msgs':msg1,  #  随机得到四条新闻
    }
    return  render(request,'index.html',context)

def home(request):
    # context = {}
    # context['hello'] = 'hello world1111'

    return render(request, 'home.html')