"""CONFIDENTIALITY URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import Home, Register, Login, logoutuser, Aboutus, Contactus, Services, Patientdetails, Feedbacks, login_view, confidential_info, Appointmentdetails, Priscription

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home, name='home'),
    path('', Register, name='register'),
    path('loginpage/', Login, name='loginpage'),
    path('logout/', logoutuser, name='logout'),
    path('aboutus', Aboutus, name='aboutus'),
    path('services', Services, name='services'),
    path('contactus', Contactus, name='contactus'),
    path('patient/', Patientdetails, name='patient'),
    path('feedback/', Feedbacks, name='feedback'),
    path('login/', login_view, name='login'),
    path('confidential/', confidential_info, name='confidential_info'),
    path('appointment/', Appointmentdetails, name='appointment'),
    path('priscription/', Priscription, name='priscription'),


]
