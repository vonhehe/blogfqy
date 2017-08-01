from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Tb20170801
# Create your views here.
def index(request):
    #msg = Tb20170801.objects.filter().exclude(imgsrc='无配图').order_by('?')[:4]
    msg = Tb20170801.objects.filter().order_by('?')[:4]
    #print(msg)
    context = {
        'news':msg,
    }
    return  HttpResponse(request,'index.html',context)

def home(request):
    # context = {}
    # context['hello'] = 'hello world1111'

    return render(request, 'home.html')