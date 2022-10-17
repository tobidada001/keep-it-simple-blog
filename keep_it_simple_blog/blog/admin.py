from django.contrib import admin
from .models import Post, Categories, Tags
# Register your models here.
admin.site.register(Post)
admin.site.register(Categories)
admin.site.register(Tags)