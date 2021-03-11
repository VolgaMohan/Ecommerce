from django.shortcuts import render
from .models import Taskadd
# Create your views here.

def home(request):
    if request.method=='POST':
        task=request.POST["task"]
        desc=request.POST["desc"]
        data=Taskadd(task=task,description=desc)
        data.save()
    return render(request,'home.html')

def task(request):
    all_task=Taskadd.objects.all()
    return render(request,'task.html',{'data':all_task})
