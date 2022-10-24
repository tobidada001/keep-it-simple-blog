from .models import Tags, Categories,Post

def context_process(request):
    tags = Tags.objects.all()
    categories = Categories.objects.all()
    posts = Post.objects.all()
    user = request.user
    return {'mytags': tags, 'categories': categories, 'posts': posts, 'user': user}
