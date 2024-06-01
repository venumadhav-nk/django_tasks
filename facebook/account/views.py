from django.shortcuts import render,HttpResponse

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
