from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Categories, Tags, Post

def index(request):
    posts = Post.objects.all()
    user = User.objects.all()
    return render(request, 'blog/index.html', {'posts': posts, 'user': user})
# Create your views here.

def archives(request):
    return render(request, 'blog/archives.html')

def blog(request):
    return render(request, 'blog/blog.html')

def demo(request):
    return render(request, 'blog/demo.html')

def page(request):
    return render(request, 'blog/page.html')

def single(request):
    return render(request, 'blog/single.html')

