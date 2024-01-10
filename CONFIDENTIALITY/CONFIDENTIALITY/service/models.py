from django.db import models

class Contact(models.Model):
    username=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    message=models.TextField()

class Patient(models.Model):
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    aadharnumber = models.CharField(max_length=12)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    maritalstatus = models.CharField(max_length=10)
    bloodgroup = models.CharField(max_length=10)
    address = models.TextField()
    symptoms = models.TextField()

    # Emergency Details
    ename = models.CharField(max_length=30)
    relation = models.CharField(max_length=30)  
    emergencynumber = models.CharField(max_length=10)

class Feedback(models.Model):
    name=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    message=models.TextField()

class Appointments(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    phoneNo = models.CharField(max_length=15)
    appointmentDate = models.DateField()
    symptoms = models.TextField()
    is_approved = models.BooleanField(default=False)

# Create your models here.
