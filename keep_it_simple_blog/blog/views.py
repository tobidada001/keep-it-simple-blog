from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from .models import Categories, Tags, Post
from django.utils import timezone
import datetime


def index(request):
    posts = Post.objects.all()
    categories = Categories.objects.all()
    tags = Tags.objects.all()
    p3 = Post.objects.filter(id=3)

    for p in p3:

        if p.post_date < timezone.now():
            print('Timezone is lesser')
        else:
            print("Timezone is greater")

    # pub_date = Post.objects.filter(p3.post_date <= timezone.now()).order_by('post_date')
    # for a in pub_date:
    #     print(a.post_title)


    for i in posts:
        if(i.post_date < timezone.now()):
            print('Date and time is Lesser than current one')
        elif i.post_date == timezone.now():
            print('Date and time are the same with the current one')
        else:
            print("They're not the same"  )

    return render(request, 'blog/index.html', {'posts': posts[:5], 'categories': categories, 'tags': tags})
# Create your views here.

def archives(request):
    post = Post.objects.all().order_by('-post_date')
    category = Categories.objects.all()
    p = Post.objects.get(id=5)

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
    first_post = Post.objects.all().first()
    last_post = Post.objects.all().last()
    
    context = {
        'post': post, 
        'mytags': mytags, 
        'first_post': first_post, 
        'last_post': last_post
    }

    return render(request, 'blog/single.html', context)

def postlist(request, pk):
    post = Categories.objects.get(category = pk)
    posts = post.categories.all()
   
    return render(request, 'blog/postlist.html', {'category_post': posts, 'post': post})

def tagposts(request, pk):
    tag = Tags.objects.get(tag_name = pk)
    tagpost = tag.tags.all()
    return render(request, 'blog/tagposts.html', {'tags': tagpost, 'tag': tag})