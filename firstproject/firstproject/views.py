from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("<h1> hello world , you are at codewithsamir homepage </h1>")
    return render(request, 'index.html')

def about(request):
    # return HttpResponse("hello world , you are at codewithsamir aboutpage")
     return render(request, 'about.html')

def contact(request):
    # return HttpResponse("hello world , you are at codewithsamir conatact page")
     return render(request, 'contact.html')