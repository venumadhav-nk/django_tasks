from django.shortcuts import render,HttpResponse

def taks1(request):
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
