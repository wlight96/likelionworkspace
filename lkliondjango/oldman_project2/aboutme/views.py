from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def aboutme(request):
    return render(request,'aboutme.html')
# Create your views here.
