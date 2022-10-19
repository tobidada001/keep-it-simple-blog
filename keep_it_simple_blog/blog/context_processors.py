from .models import Tags, Categories,Post

def context_process(request):
    tags = Tags.objects.all()
    categories = Categories.objects.all()
    posts = Post.objects.all()
    return {'mytags': tags, 'categories': categories, 'posts': posts}
