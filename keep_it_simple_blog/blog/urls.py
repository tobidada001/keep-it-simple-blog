from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = "index"),
    path('archives', views.archives, name = "archives"),
    path('blog/', views.blog, name = "blog"),
    path('demo', views.demo, name = "demo"),
    path('page', views.page, name = "page"),
    path('blog/<str:pk>', views.single, name = "blog_single"),
    path('post-category/<str:pk>', views.postlist, name="postlist"),
    path('tags/<str:pk>', views.tagposts, name="tagposts"),
]