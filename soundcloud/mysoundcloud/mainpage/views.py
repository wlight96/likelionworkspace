from django.shortcuts import render, redirect

def home(request):
    return render(request, 'main.html')


# Create your views here.
