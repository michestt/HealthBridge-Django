from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


class Categories(models.Model):
    category = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.category


class Post(models.Model):
    category = models.ForeignKey(Categories, related_name='posts', on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, max_length=100)
    description = models.TextField(max_length=10000)
    content = models.TextField(default='(empty)')
    published = models.DateField(auto_now_add=True)
    pic = models.ImageField(upload_to='pics', null=True, blank=True, default='default.png')
    enabled = models.BooleanField(default=True)
    tags = TaggableManager()
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.email


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')
