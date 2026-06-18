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

    r = ""
    if 180 <= c <= 200:
        r = "you scored A+"
    elif 150 <= c < 180:
        r = "you scored B+"
    elif 100 <= c < 150:
        r = "you scored C+"
    elif 50 <= c < 100:
        r = "you scored D+"
    else:
        r = "better luck next time"
    return render(request,'ans.html',{'subject1':a,'subject2':b,'total':c,'result':r})

def saveSessionData(request):
    request.session['username'] = "Jeet"
    return HttpResponse("session created")

def getSessionData(request):
    if request.session.has_key('username'):
        msg = request.session['username']
        return HttpResponse(msg)
    else:
        return HttpResponse("session not found")

def removeSessionData(request):
    del request.session['username']
    return HttpResponse("session deleted")