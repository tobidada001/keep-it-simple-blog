from .models import Categories, Post
from taggit.models import Tag
import random


def context_process(request):
    tags = Tag.objects.all()[:10]
    categories = Categories.objects.all()[:10]
    posts = Post.published.all()[:5]
    recommended_post = []
    
    if(len(Post.published.all()) > 0):
        recommended_post = random.choice(Post.published.all())
        
    user = request.user
    thumb_list = [1, 2, 3, 4, 5, 6, 7, 8]
    social_links = [{'facebook':'https://www.facebook.com/tobidada940'}, {'youtube': 'https://www.youtube.com/codingwithmitch'}, {'telegram': 'https://www.telegram.org/tobbs101'},
    
            {'twitter':'https://www.twitter.com/tobidada14'}, {'vimeo': 'https://www.facebook.com/tobidada940'}, {'linkedin': 'https://www.twitter.com/tobidada14'},
            {'instagram': 'https://www.telegram.org/tobbs101'}]
    
    return {'tags': tags, 'categories': categories, 'posts': posts, 'user': user, 'thumbs': thumb_list, 'social_links': social_links, 
                'recommended': recommended_post}
