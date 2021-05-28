from datetime import time
from django.shortcuts import redirect,render
from .models import Oldman_blog,Oldman_notice
from django.utils import timezone
# Create your views here.

def home(request):
    blogs = Oldman_blog.objects
    notices = Oldman_notice.objects
    return render(request,'home.html',{'blogs':blogs, 'notices':notices})

def detail(request,blog_id):
    blog_detail = Oldman_blog.objects.get(id = blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Oldman_blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def delete(request, blog_id):
    Oldman_blog.objects.get(id = blog_id).delete()
    return redirect('/')

def edit(request, blog_id):
    blog = Oldman_blog.objects.get(id = blog_id)
    return render(request, 'edit.html', {'blog': blog})

def update(request, blog_id):
    blog = Oldman_blog.objects.get(id = blog_id)
    blog.title = request.POST.get('title')
    blog.body = request.POST.get('body')
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))