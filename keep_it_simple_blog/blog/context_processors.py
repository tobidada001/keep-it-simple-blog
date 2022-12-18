from .models import Tags, Categories,Post

def context_process(request):
    tags = Tags.objects.all()
    categories = Categories.objects.all()
    posts = Post.objects.all()
    user = request.user
    thumb_list = [1, 2, 3, 4, 5, 6, 7, 8]
    social_links = [{'facebook':'https://www.facebook.com/tobidada940'}, {'youtube': 'https://www.youtube.com/codingwithmitch'}, {'telegram': 'https://www.telegram.org/tobbs101'},
    
            {'twitter':'https://www.twitter.com/tobidada14'}, {'vimeo': 'https://www.facebook.com/tobidada940'}, {'linkedin': 'https://www.twitter.com/tobidada14'},
            {'instagram': 'https://www.telegram.org/tobbs101'}]
    
    for i in social_links:
        print(i)

    return {'mytags': tags, 'categories': categories, 'posts': posts, 'user': user, 'thumbs': thumb_list, 'social_links': social_links}
