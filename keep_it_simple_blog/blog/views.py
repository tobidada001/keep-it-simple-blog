from django.shortcuts import render

def index(request):

    return render(request, 'blog/index.html')
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

