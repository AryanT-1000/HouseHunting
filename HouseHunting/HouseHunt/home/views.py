from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/home1.html')

def featured(request):
    return render(request, 'home/featured.html')