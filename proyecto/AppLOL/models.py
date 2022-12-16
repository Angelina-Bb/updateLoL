from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    subtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    body = models.TextField()
    creator = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created_at',)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Campeones(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    slug = models.SlugField()
    image = models.ImageField()
    body = models.TextField()
    creator = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created_at',)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)        