from django.contrib import admin
from .models import Post, Categories, Tags, Comments, Replies
# Register your models here.
admin.site.register(Post)
admin.site.register(Categories)
admin.site.register(Tags)
admin.site.register(Comments)
admin.site.register(Replies)