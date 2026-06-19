from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('home', views.homepage),
    path('about',views.aboutpage),
    path('contact',views.contactpage),
    path('gallery',views.gallerypage),
    path('shop',views.shoppage),
    path('contactprocess',views.contactprocess),
    path('saveSession',views.saveSessionData),
    path('getSession',views.getSessionData),
    path('removeSession', views.removeSessionData),
    path('login',views.loginPage),
    path('loginProcess',views.loginProcess),
    path('dashboard',views.dashboard),
    path('logout',views.logout),
    path('contactus',views.contactPageView),
    path('process',views.mailsendprocess),
    path('student',views.studentpage),
    path('add-student-process',views.addstudent),
    path('getstudent',views.getstudent),
    path('deletestudent/<int:id>',views.deletestudent),
]