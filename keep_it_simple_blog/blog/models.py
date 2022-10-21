from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Categories(models.Model):
    category = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Categories")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.category

class Tags(models.Model):
    tag_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Tags")
        verbose_name_plural = ("Tags")

    def __str__(self):
        return self.tag_name

class Post(models.Model):

    post_title = models.CharField(max_length=100)
    post_body = models.TextField(null=True)
    category = models.ForeignKey(Categories, related_name='categories', on_delete=models.CASCADE)
    author = models.ForeignKey(User,related_name= "author", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags, related_name = 'tags')
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.post_title

