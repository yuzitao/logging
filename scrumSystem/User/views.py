from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from User.logsave import wrapper
from User.models import Log


@wrapper
def index(request):
    logs = Log.objects.all()
    return render(request,'index.html',context={'logs':logs})

@wrapper
def user(request):
    logs = Log.objects.all()
    return render(request, 'index.html', context={'logs': logs})
