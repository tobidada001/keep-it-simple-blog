from django.db import models
from django.contrib.auth.models import User
import datetime
from ckeditor_uploader.fields import RichTextUploadingField
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
    post_body = RichTextUploadingField()
    cover = models.ImageField(upload_to='images', blank=True)
    category = models.ForeignKey(Categories, related_name='categories', on_delete=models.CASCADE)
    author = models.ForeignKey(User,related_name= "author", blank=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags, related_name = 'tags')
    post_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default = 1)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.post_title


class Comments(models.Model):
    name = models.CharField(max_length=70)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    comment = models.CharField(max_length=3000)
    post = models.ForeignKey(Post, related_name= "topic", on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Comments'
        verbose_name_plural = 'Comments'


class Replies(models.Model):
    name = models.CharField(max_length=70)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    website = models.URLField(max_length=200)
    reply = models.CharField(max_length=3000)
    main_comment = models.ForeignKey(Comments, related_name= "main_comment", on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Replied to: " + str(self.main_comment)

    class Meta:
        verbose_name = 'Replies'
        verbose_name_plural = 'Replies'


class Contact(models.Model):

    contact_name = models.CharField('Name', max_length=100)
    contact_email = models.EmailField("Email Address", max_length=254)
    subject = models.CharField('Subject', max_length=80)
    message = models.CharField('Your Message' , max_length=2000)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
    
    def __str__(self):
        return self.contact_name + ' :: ' + self.subject

class newdef(models.Model):
    myname = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='static/', default= 1)
    mydata = RichTextUploadingField()
   