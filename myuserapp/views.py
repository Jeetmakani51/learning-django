from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from . models import Student
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

def loginPage(request):
    return render(request,'login.html')

def loginProcess(request):
    txt1 = request.POST['myemail']
    request.session['emaillogin'] = txt1
    if(request.session.has_key('emaillogin')):
        return render(request,'dashboard.html')
    else:
        return redirect(request,'login.html')
    
def dashboard(request):
    if request.session.has_key('emaillogin'):
        return render(request,'dashboard.html')
    else:
        return redirect(request,'login.html')
    
def logout(request):
    del request.session['emaillogin']
    return redirect(loginPage)

def contactPageView(request):
    return render(request,'contactus.html')

def mailsendprocess(request):
    subject = request.POST['txt2']
    message = request.POST['txt3']
    recipient_list = ['j@gmail.com']
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject,message,email_from,recipient_list)
    return HttpResponse('Male Sent')

def studentpage(request):
    return render(request,'student.html')

def addstudent(request):
    txt1 = request.POST['txt1']
    txt2 = request.POST['txt2']
    txt3 = request.POST['txt3']

    send_mail(
        "New Student Registration",  # Subject
        f"Name : {txt1}\n"
        f"Number : {txt2}\n"
        f"Email : {txt3}",
        settings.EMAIL_HOST_USER,    # From email
        [settings.EMAIL_HOST_USER],  # Recipient list
        fail_silently=False,
    )

    return render(request, "student.html")