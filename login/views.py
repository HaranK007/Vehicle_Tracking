from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.urls import path,include
# import psycopg2

# Create your views here.

def login(request):
    return render(request,'login.html')

def validateLogin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            print('success')
            return redirect('dashboard')
        else:
            return redirect('/')
    else:
        return redirect('/')