# Generated by Django 4.1 on 2022-11-03 11:36

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Categories',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.CharField(max_length=3000)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Comments',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=100, verbose_name='Name')),
                ('contact_email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('subject', models.CharField(max_length=80, verbose_name='Subject')),
                ('message', models.CharField(max_length=2000, verbose_name='Your Message')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='newdef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myname', models.CharField(max_length=50)),
                ('cover', models.ImageField(default=1, upload_to='static/')),
                ('mydata', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tags',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('reply', models.CharField(max_length=3000)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('main_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_comment', to='blog.comments')),
            ],
            options={
                'verbose_name': 'Replies',
                'verbose_name_plural': 'Replies',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=100)),
                ('post_body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('cover', models.ImageField(blank=True, upload_to='images')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(default=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='blog.categories')),
                ('tags', models.ManyToManyField(related_name='tags', to='blog.tags')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic', to='blog.post'),
        ),
    ]
