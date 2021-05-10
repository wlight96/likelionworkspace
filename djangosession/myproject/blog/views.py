from django.shortcuts import render
from .models import Blog
# Create your views here.
def hello(request):
    return render(request,"hello.html")

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs}) 