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

def contactprocess(request):
    a = int(request.POST['txt1'])
    b = int(request.POST['txt2'])
    c = a + b
    msg = "A value is",a,"B value is",b,"Sum is ",c

    r = ""
    if c == 30:
        r = "if condition called"
    elif c > 30:
        r = "elif condition called"
    else:
        r = "else condition called"
    return render(request,'ans.html',{'mya':a,'myb':b,'myc':c,'myr':r})
