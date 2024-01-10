from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from service.models import Contact, Patient, Feedback
from django.core.exceptions import ObjectDoesNotExist
from service.models import Appointments

@login_required
def Home(request):
    return render(request,'Home.html', {})
    
def Register(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        phno = request.POST.get('number')
        aadharnumber = request.POST.get('aadharnumber')
        password = request.POST.get('password')

        new_user = User.objects.create_user(name, email, password)
        new_user.phno = phno
        new_user.aadharnumber=aadharnumber
        new_user.save()
        return redirect('loginpage')
    return render(request,'Register.html', {})

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Error, user does not exist')
    return render(request,'Login.html', {})

def logoutuser(request):
    logout(request)
    return redirect('loginpage')

def Aboutus(request):
    return render(request,'Aboutus.html', {})

def Services(request):
    return render(request,'Services.html', {})

def Contactus(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        message = request.POST['message']
        ins = Contact(username=username,message=message, email=email)
        ins.save()
        print("ok")
    return render(request,'Contactus.html', {})

def Patientdetails(request):
    if request.method == "POST":
        name = request.POST['name']
        gender = request.POST['gender']
        date_of_birth = request.POST['date_of_birth']
        aadharnumber = request.POST['aadharnumber']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        maritalstatus = request.POST['maritalstatus']
        bloodgroup = request.POST['bloodgroup']
        address = request.POST['address']
        symptoms = request.POST['symptoms']

        ename = request.POST['ename']
        relation = request.POST['relation']
        emergencynumber = request.POST['emergencynumber']
        
        ins = Patient(name=name, gender=gender, date_of_birth=date_of_birth, aadharnumber=aadharnumber, email=email, phonenumber=phonenumber, 
        maritalstatus=maritalstatus, bloodgroup=bloodgroup, address=address, symptoms=symptoms, ename=ename, relation=relation, emergencynumber=emergencynumber)
        ins.save()
    return render(request, 'Patient.html', {})

def Feedbacks(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        ins = Feedback(name=name,email=email, message=message)
        ins.save()
        print("ok")
    return render(request,'Feedback.html', {})

# 

def login_view(request):
    if request.method == 'POST':
        passwords = request.POST.get('password')
        username = request.POST.get('username')
        # Replace 'your_password' with your desired password
        user = authenticate(request, username=username, password=passwords)
        if user is not None:
            login(request, user)
            return redirect('priscription')  # Redirect to the confidential information page

    return render(request, 'password_login.html')

@login_required(login_url='/login/')  # Redirect to the login page if the user is not authenticated
def confidential_info(request):
    return render(request, 'confidential_info.html')

def Appointmentdetails(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        phoneNo = request.POST.get('phoneNo')
        appointmentDate = request.POST.get('appointmentDate')
        symptoms = request.POST.get('symptoms')

        new_appointment = Appointments.objects.create(
            name=name,
            age=age,
            phoneNo=phoneNo,
            appointmentDate=appointmentDate,
            symptoms=symptoms
        )

        # You can add additional logic here if needed

        return redirect('appointment')
    return render(request, 'Appointment.html', {})
@login_required
def Priscription(request):
    # Fetch only approved appointments
    approved_appointments = Appointments.objects.filter(is_approved=True)

    context = {'approved_appointments': approved_appointments}
    return render(request, 'Priscription.html', context)
