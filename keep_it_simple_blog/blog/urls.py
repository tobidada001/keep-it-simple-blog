from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('', views.index, name = "index"),
    path('archives/', views.archives, name = "archives"),
    path('blog/', views.blog, name = "blog"),
    path('about', TemplateView.as_view(template_name = 'blog/about.html'), name = "about"),
    path('blog/<int:year>/<int:month>/<int:day>/<slug:pk>', views.single, name = "blog_single"),
    path('post-category/<str:pk>', views.postlist, name="postlist"),
    path('tags/<slug:pk>', views.tagposts, name="tagposts"),
    path('search/', views.search, name= "process_search"),
    path('login/', views.loginuser, name="login"),
    path('post/edit/drafts', views.DraftListView.as_view(), name = 'drafts'),
    path('logout/', views.logoutuser, name="logout"),
    path('addcomment/<int:id>/<slug:pk>', views.addcomment, name='addcomment'),
    path('delete-comment/<int:id>', views.delete_comment, name='delete_comment'),
    path('approve-comment/<int:id>', views.approve_comment, name='approve_comment'),
    path('privacy/', TemplateView.as_view(template_name = 'blog/privacy.html'), name='privacy'),
    path('contact/', views.contact, name='contact'),
    path('post/edit/new', views.newpost, name = 'newpost'),
    path('post/edit/<slug:pk>', views.editpost, name = 'editpost'),
    path('post/edit/delete/<slug:pk>', views.deletepost, name='deletepost'),
    path('post/edit/publish/<slug:pk>', views.publish_post, name = 'publish_post')
]