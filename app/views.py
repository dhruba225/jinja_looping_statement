from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def loop(request):
    d={'name':'DHRUBA','age':23}
    return render(request,'loop.html',context=d)