from django.shortcuts import render
from .models import Item

# Create your views here.

def home(request):
    context= {
        'items': Item.objects.all()
    }
    print(context)
    return render(request,'registration/home.html',context)

def cart(request):
    context={}
    return render(request,'store/cart.html')

def checkout(request):
    context={}
    return render(request,'store/checkout.html')