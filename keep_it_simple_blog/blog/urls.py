from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = "index"),
    path('archives', views.archives, name = "archives"),
    path('blog/', views.blog, name = "blog"),
    path('demo', views.demo, name = "demo"),
    path('about', views.about, name = "about"),
    path('blog/<str:pk>', views.single, name = "blog_single"),
    path('post-category/<str:pk>', views.postlist, name="postlist"),
    path('tags/<str:pk>', views.tagposts, name="tagposts"),
    path('search', views.search, name= "process_search"),
    path('login', views.loginuser, name="login"),
    path('logout', views.logoutuser, name="logout"),
    path('addcomment/<str:pk>', views.addcomment, name='addcomment')
]