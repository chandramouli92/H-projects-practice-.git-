from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>wekcome my new app </h1>")

def home(request):
    return render(request,"cm1/sam1.html")

def tem(request):
    return render(request,"child.html")

def sam(request):
    return render(request,"cm1/sample.html")