from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib import auth
from .models import Categories, Tags, Post, Comments
from django.utils import timezone
import datetime
from django.db.models import Q

def loginuser(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username = username).exists():
            print('user already exists')
            user = auth.authenticate(username = username, password=password)
            print('User is now authenticated in First IF')
            print(user)
            if user.is_authenticated:
                login(request, user)
                print('User is now logged in.')
                return redirect('/')
            else:
                return redirect('/')
        else:
            a = User.objects.create_user(username = username, password = password)
            a.save()
            print(a)
            user = auth.authenticate(username=username, password = password)
            
            if user is not None:
                login(request, user)
                print('User is now created and logged in.')
                return redirect('/')

    return render(request, 'blog/login.html')

def logoutuser(request):
    logout(request)
    return redirect('/')


def index(request):
    posts = Post.objects.all()
    categories = Categories.objects.all()
    tags = Tags.objects.all()
    print(request.user)

    return render(request, 'blog/index.html', {'posts': posts[:5], 'categories': categories, 'tags': tags})
# Create your views here.

def archives(request):
    post = Post.objects.all().order_by('-post_date')
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
    post_comments = post.topic.all()

    nocs = 0
    for p in post_comments:
        nocs = nocs + 1
        for reply in p.main_comment.all():
            nocs = nocs + 1

    context = { 
        'post': post, 
        'mytags': mytags, 
        'comments': post_comments,
        'totalcomments': nocs
    }

    if request.method == 'POST':
        comment = request.POST.get('cMessage')
        
        new_comment = Comments(name = request.user.first_name + request.user.last_name, 
        username = request.user.username, email = request.user.email, comment = comment, post = post )

        new_comment.save()
        return redirect('blog_single', post.post_title)
    
    return render(request, 'blog/single.html', context)

def postlist(request, pk):
    post = Categories.objects.get(category = pk)
    posts = post.categories.all()
   
    return render(request, 'blog/postlist.html', {'category_post': posts, 'post': post})

def tagposts(request, pk):
    tag = Tags.objects.get(tag_name = pk)
    tagpost = tag.tags.all()
    return render(request, 'blog/tagposts.html', {'tags': tagpost, 'tag': tag})

def search(request):
    search = request.GET['searchbox']
    posts = Post.objects.filter(Q(post_title__icontains=search) | Q(post_body__icontains=search)) 
    
    return render(request, 'blog/search.html', {'posts': posts})
    