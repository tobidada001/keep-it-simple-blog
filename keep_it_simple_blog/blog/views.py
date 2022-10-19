from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from .models import Categories, Tags, Post

def index(request):
    posts = Post.objects.all()
    categories = Categories.objects.all()
    tags = Tags.objects.all()
    return render(request, 'blog/index.html', {'posts': posts[:5], 'categories': categories, 'tags': tags})
# Create your views here.

def archives(request):
    post = Post.objects.all().order_by('-post_date').values()
    category = Categories.objects.all()
    return render(request, 'blog/archives.html', {'posts': post, 'cat': category})

def blog(request):
    posts = Post.objects.all()
    categories = Categories.objects.all()
    tags = Tags.objects.all()
    return render(request, 'blog/blog.html',{'posts': posts[:5], 'categories': categories, 'tags': tags})

def demo(request):
    return render(request, 'blog/demo.html')

def page(request):
    return render(request, 'blog/page.html')

def single(request, pk):
    post = Post.objects.get(post_title = pk)
    mytags = post.tags.all()
    
    return render(request, 'blog/single.html', {'post': post, 'mytags': mytags})

def postlist(request, pk):
    post = Categories.objects.get(category = pk)
    posts = post.categories.all()
   
    return render(request, 'blog/postlist.html', {'category_post': posts, 'post': post})

def tagposts(request, pk):
    tag = Tags.objects.get(tag_name = pk)
    tagpost = tag.tags.all()
    return render(request, 'blog/tagposts.html', {'tags': tagpost, 'tag': tag})