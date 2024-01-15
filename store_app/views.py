from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import Department

# Create your views here.


def home(request):
    return render(request, 'home.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request, "form.html")
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password1']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register')


    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def depart(request):
   dict_dept={
        'dept' : Department.objects.all()
    }

   return render(request,"depart.html",dict_dept)

def new_form(request):
    if request.method == 'POST':
        messages.info(request, "Order Placed")
        return redirect('new_form')
    return render(request,"new_form.html")



