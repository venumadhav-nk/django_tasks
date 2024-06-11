from django.shortcuts import render,HttpResponse
from .models import student

def task1(request):
    context=[
        {
            'name':'nandhakumar',
            'age':'20',
            'place':'puttur',
            'role':'student'
        }
    ]
    return render(request,'home.html',{'context':context})

# Create your views here.

def task2(request,father,son):
    
    context={'father':father,'son':son}
    return render(request,'home2.html',context)

def fruit(request):
    fruit=[
        {
            'fruit':'apple',
            'quantity':'1kg',
            'rate':'200', 
        },
         {
            'fruit':'orange',
            'quantity':'1kg',
            'rate':'400', 
        },
         {
            'fruit':'mango',
            'quantity':'1kg',
            'rate':'150', 
        }
    ]
    return render(request ,'home3.html',{'fruit':fruit})

def nav(request):
    return render(request,'nav.html')

def stu(request):
    students=student.objects.all()
    return render(request,'base.html',{'student':students})

