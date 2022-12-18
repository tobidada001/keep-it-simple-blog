from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .models import Categories, Tags, Post, Comments
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import ContactForm, NewPost



def loginuser(request):
   
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username = username).exists():
            user = auth.authenticate(username = username, password=password)
            if user.is_authenticated:
                login(request, user)
                return redirect('/')
            else:
                return redirect('login')
        else:
            a = User.objects.create_user(username = username, password = password)
            a.save()
            user = auth.authenticate(username=username, password = password)
            
            if user is not None:
                login(request, user)

                if user.is_authenticated:
                    return redirect('/')
            else:
                return redirect('login')
        

    return render(request, 'blog/login.html')

def logoutuser(request):
    logout(request)
    return redirect('/')


def index(request):
    posts = Post.objects.all().order_by('post_date')
    categories = Categories.objects.all()
    tags = Tags.objects.all()

    print(request.user)

    return render(request, 'blog/index.html', {'posts': posts, 'categories': categories, 'tags': tags})
# Create your views here.

def archives(request):
    post = Post.objects.all().order_by('-post_date')
    category = Categories.objects.all()

    return render(request, 'blog/archives.html', {'posts': post, 'cat': category})

def blog(request):
    posts = Post.objects.all().order_by('-post_date')
    categories = Categories.objects.all()
    tags = Tags.objects.all()

    page = Paginator(posts, 5)
    page_num = request.GET.get('page')
    getpage = page.get_page(page_num)

    return render(request, 'blog/blog.html',{'page': getpage, 'categories': categories, 'tags': tags})


def about(request):
    return render(request, 'blog/about.html')


def single(request, pk):
    post = get_object_or_404(Post, post_title = pk)
    
    mytags = post.tags.all()
    post_comments = post.topic.all()

    nocs = 0
    for p in post_comments:
        nocs = nocs + 1
        for reply in p.main_comment.all():
            nocs = nocs + 1

    context = {'post': post, 'mytags': mytags, 'comments': post_comments, 'totalcomments': nocs}

    return render(request, 'blog/single.html', context)


def postlist(request, pk):
    post = get_object_or_404(Categories, category = pk)
    posts = post.categories.all()
   
    return render(request, 'blog/postlist.html', {'category_post': posts, 'post': post})


def tagposts(request, pk):
    tag = get_object_or_404(Tags, tag_name = pk)
    tagpost = tag.tags.all()
    return render(request, 'blog/tagposts.html', {'tags': tagpost, 'tag': tag})


def search(request):
    search = request.GET['searchbox']
    posts = Post.objects.filter(Q(post_title__icontains=search) | Q(post_body__icontains=search)) 
    
    return render(request, 'blog/search.html', {'posts': posts})


def addcomment(request,pk):
    post = get_object_or_404(Post, post_title = pk)
    print(post)

    if request.method == 'POST':
        comment = request.POST.get('cMessage')
        print('Now in the post method')
        new_comment = Comments(name = request.user.first_name + request.user.last_name, 
        username = request.user.username, email = request.user.email, comment = comment, post = post )

        new_comment.save()
        print('New comment saved.')

        return redirect('blog_single', post.post_title)

    elif request.method == 'GET':
        print('Request is GET')
        print('It seems an error occured')
        return redirect('blog_single', post.post_title)


def privacy(request):
    
    return render(request, 'blog/privacy.html')


def contact(request):
    myform = ContactForm()

    if request.method == 'POST':
        myform = ContactForm(request.POST)

        if myform.is_valid():
            myform.save()
            messages.info(request, 'Thank you for the feedback! Your message has been successfully sent!')
            return redirect('contact')
        else:
            print('Form is not valid')
            for msg in myform.error_messages:

                messages.info(request,'Ooops! An error occured! Please try again later.')
    else:
        myform = ContactForm()
    return render(request, 'blog/contact.html', {'myform': myform})


def newpost(request):
    if not request.user.is_superuser:
        return redirect('/')
    newpost = NewPost(request.FILES)
    
    if request.method == 'POST':
        print('My FILES: ', request.FILES)
        newpost = NewPost(request.POST, request.FILES)
        if newpost.is_valid():
            post_title = newpost.cleaned_data.get('post_title')
            post_body = newpost.cleaned_data.get('post_body')
            cover = newpost.cleaned_data.get('cover')
            category = newpost.cleaned_data.get('category')
            tags = newpost.cleaned_data.get('tags')

            print('Cover: ',cover)
            new_post = Post(post_title = post_title, post_body = post_body,
            category = category, author = request.user, cover = cover)
            new_post.save()
           
            for tag in tags:
                new_post.tags.add(tag)
             
            new_post.save()
            return redirect('blog_single', new_post.post_title)
        else:
            print('Data is not Valid')
    else:
        newpost = NewPost()       

    return render(request, 'blog/newpost.html', {'newpostform': newpost})


def deletepost(request, pk):
    if not request.user.is_superuser:
        return redirect('/')
    post = get_object_or_404(Post, post_title = pk)
    post.delete()

    return redirect('/')

def editpost(request, pk):
    if not request.user.is_superuser:
        return redirect('/')
    post = get_object_or_404(Post, post_title = pk)
    
    context = { 'post_title': post.post_title, 'post_body': post.post_body,  'author': post.author,
        'category': post.category, 'tags': post.tags.all(),}
    
    newpost = NewPost(context, {'cover': post.cover}) 
    
    if request.method == 'POST':
        
        newpost = NewPost(request.POST, request.FILES)
        if newpost.is_valid():
            print('NewPostForm is valid\n\n')
            post.post_title = newpost.cleaned_data.get('post_title')
            post.post_body = newpost.cleaned_data.get('post_body')
            post.author = request.user
            newcover =  newpost.cleaned_data.get('cover')
            
            if newcover:
                post.cover = newcover 
            else:
                post.cover = post.cover
            post.category = newpost.cleaned_data['category']
            post.tags.set(newpost.cleaned_data['tags'])
            post.save()
            newpost = NewPost()

            return redirect('blog_single', post.post_title)
        else:
            print('Data is not Valid')

    return render(request, 'blog/editpost.html', {'newpostform': newpost, 'post': post})