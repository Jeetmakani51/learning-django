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
    if c > 180 and c < 200:
        r = "you scored A+"
    elif c > 150 and c < 180:
        r = "you scored B+"
    elif c > 100 and c < 150:
        r = "you scored C+"
    elif c > 50 and c < 100:
        r = "you scored D+"
    else:
        r = "better luck next time"
    return render(request,'ans.html',{'subject1':a,'subject2':b,'total':c,'result':r})
