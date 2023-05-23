from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def munyao(request):
    return HttpResponse("General Line")

def calc(request):
    return HttpResponse(1+1)

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
