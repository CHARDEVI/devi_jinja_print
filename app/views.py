from django.shortcuts import render

# Create your views here.

def devi(request):
    return render(request,'devi.html',context={'name':'CHARISHMA'})
