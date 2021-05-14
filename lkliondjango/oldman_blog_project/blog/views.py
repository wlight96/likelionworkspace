from django.shortcuts import render
from .models import Blog
from .models import Notice
# Create your views here.
def blog(request):
    blogs = Blog.objects
    notices = Notice.objects
    return render(request,"blog.html",{'blogs':blogs, 'notices':notices})

    