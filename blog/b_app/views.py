from django.shortcuts import render,redirect
from .form import signinform
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.core.mail import send_mail
from .models import Profile
from django.contrib import messages
import math, random

from django.views.generic import ListView
# Create your views here.

def signinview(request):
    if request.method=="POST":
        form = signinform(request.POST)
        if form.is_valid():
            form.save
            return redirect("login")
    else:
        form = signinform()
        return render(request,"signin.html",{"form":form})

def Login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if user is not None:
            Login(request, user)
            return redirect("home")
        else:
            return redirect("login")

    return render(request, "login.html")


def home(request):
    post=Profile.objects.all()

    return render(request,"base.html",{'post':post})



def otp(request):
    return render(request, "otp.html")


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


def send_otp(request):
    email = request.GET.get("email")
    print(email)
    o = generateOTP()
    htmlgen = '<p>Your OTP is <strong>o</strong></p>'
    send_mail('OTP request', o, '<your gmail id>', [email], fail_silently=False, html_message=htmlgen)
    return HttpResponse(o)





