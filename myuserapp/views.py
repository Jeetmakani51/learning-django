from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return render(request,'home.html')

def aboutpage(request):
    return render(request,'about.html')

def contactpage(request):
    return render(request,'contact.html')

def gallerypage(request):
    return render(request,'gallery.html')

def shoppage(request):
    return render(request,'shop.html')