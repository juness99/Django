from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")
    
def greeting(request, name):
    return render(request,"greeting.html",{'name':name})