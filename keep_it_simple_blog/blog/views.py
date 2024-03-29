from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .models import Categories, Post, Comments
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import ContactForm, NewPost
from django.utils.text import slugify
from django.views.generic import ListView
from pprint import pprint as pp
from taggit.models import Tag

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
            if username and password:
                a = User.objects.create_user(username = username, password = password)
                a.save()
                user = auth.authenticate(username=username, password = password)
            
                if user is not None:
                    login(request, user)
                    return redirect('/')
            else:
                return redirect('login')
        

    return render(request, 'blog/login.html')

def logoutuser(request):
    logout(request)
    return redirect('/')


def index(request):
    posts = Post.published.all()[:5]
    categories = Categories.objects.all()
    tags = Tag.objects.all()[:10]
    
    return render(request, 'blog/index.html', {'posts': posts, 'categories': categories, 'tags': tags})


def archives(request):
    post = Post.objects.all().order_by('-post_date')
    
    category = Categories.objects.all()

    return render(request, 'blog/archives.html', {'posts': post, 'cat': category})

def blog(request):
    posts = Post.published.all().order_by('-post_date')
    categories = Categories.objects.all()
    tags = Tag.objects.all()

    page = Paginator(posts, 5)
    page_num = request.GET.get('page')
    getpage = page.get_page(page_num)

    return render(request, 'blog/blog.html',{'page': getpage, 'categories': categories, 'tags': tags})


def single(request, year, month, day, pk):
    post = get_object_or_404(Post, post_date__year = year,  post_date__month = month, post_date__day=day, slug = pk)
    post_comments = None
    nocs = 0
    if request.user.is_superuser:
        post_comments = post.topic.all()
        nocs = int(post_comments.count())
    else:
        post_comments = post.topic.filter(approval_status = True)
        nocs = int(post_comments.count())

    all_post_comments = post.topic.all()
    
    for reply in post_comments:
        for r in reply.main_comment.all():
            nocs = nocs + 1
   
    context = {'post': post, 'comments': post_comments, 'totalcomments': nocs, 'all_comments': all_post_comments }

    return render(request, 'blog/single.html', context)


def postlist(request, pk):
    post = get_object_or_404(Categories, category = pk)
    posts = post.categories.all()
   
    return render(request, 'blog/postlist.html', {'category_post': posts, 'post': post})


def tagposts(request, pk):
    tag = get_object_or_404(Tag, slug = pk)
    tagpost = Post.objects.filter(tagsagain__slug = tag.slug)
    
    return render(request, 'blog/tagposts.html', {'tags': tagpost, 'tag': tag})


def search(request):
    search = request.GET['searchbox']
    posts = Post.objects.filter(Q(post_title__icontains=search) | Q(post_body__icontains=search)) 
    
    return render(request, 'blog/search.html', {'posts': posts})

def delete_comment(request, id):
    comment = Comments.objects.get(id = id)
    comment.delete()
    return redirect(comment.post.get_absolute_url())


def approve_comment(request, id):
    comment = Comments.objects.get(id = id)
    comment.approval_status = True
    comment.save()
    return redirect(comment.post.get_absolute_url())

def addcomment(request, id, pk):
    post = get_object_or_404(Post, id= id, slug = pk)

    if request.method == 'POST':
        comment = request.POST.get('cMessage')
        if not comment:
            return redirect(request.path)

        new_comment = Comments(name = request.user.first_name + request.user.last_name, 
        username = request.user.username, email = request.user.email, comment = comment, post = post)

        if request.user.is_superuser:
            new_comment.approval_status = True

        
        new_comment.save()

        if not request.user.is_superuser:
            request.session['pending'] = 'Your comment is awaiting admin approval...'

            if new_comment.approval_status == True:
                del request.session['pending']
                
        return redirect(post.get_absolute_url())

    return redirect(post.get_absolute_url())


def contact(request):
    myform = ContactForm()

    if request.method == 'POST':
        myform = ContactForm(request.POST)

        if myform.is_valid():
            myform.save()
            messages.info(request, 'Thank you for the feedback! Your message has been successfully sent!')
            return redirect('contact')
        else:
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
        
        newpost = NewPost(request.POST, request.FILES)
        try:
            if newpost.is_valid():
                new = newpost.save(commit = False) 
                post_title = newpost.cleaned_data.get('post_title')
                slug = slugify(str(post_title))

                if Post.objects.filter(slug = slug).exists():
                    messages.error(request, 'This post url slug already exists. Please make a few changes to your post title.')
                    return redirect (request.path)

                new.slug = slug
                new.author = request.user
                
                if 'draft' in request.POST:
                    new.status = False
                    newpost.save()
                    return redirect('/')

                newpost.save()
                return redirect(newpost.get_absolute_url())
            else:
                pass
        except BaseException:
            return redirect('/')
    else:
        newpost = NewPost()       

    return render(request, 'blog/newpost.html', {'newpostform': newpost})


def deletepost(request, pk):
    if not request.user.is_superuser:
        return redirect('/')
    post = get_object_or_404(Post, slug = pk)
    post.delete()

    return redirect('/')

def editpost(request, pk):
    post = None
    if not request.user.is_superuser:
        return redirect('/')
    try:
        post = Post.objects.get(slug = pk)
    except Post.DoesNotExist:
        raise Http404
    
    context = { 'post_title': post.post_title, 'post_body': post.post_body,  'author': post.author,
        'category': post.category, 'tagsagain': post.tagsagain.all(),}
    
    newpost = NewPost(context, {'cover': post.cover}) 
    
    if request.method == 'POST':
        
        newpost = NewPost(request.POST, request.FILES)
        if newpost.is_valid():
            
            post.post_title = newpost.cleaned_data.get('post_title')
            post.post_body = newpost.cleaned_data.get('post_body')
            post.author = request.user
            newcover =  newpost.cleaned_data.get('cover')
            
            if newcover:
                post.cover = newcover 
            else:
                post.cover = post.cover
            post.category = newpost.cleaned_data['category']
            post.tagsagain.set(newpost.cleaned_data['tagsagain'])
            post.save()
            # newpost.save_m2m()
            newpost = NewPost()

            return redirect(post.get_absolute_url())
        else:
            pass

    return render(request, 'blog/editpost.html', {'newpostform': newpost, 'post': post})


class DraftListView(ListView):
    queryset = Post.objects.filter(status = False)
    template_name = "blog/drafts.html"
    context_object_name= 'unpublished'

def publish_post(request, pk):
    post = Post.objects.get(slug =pk)
    post.status = True
    post.save()
    return redirect('drafts')

def error404(request, exception):
    return render(request, 'blog/error404.html')