
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, SlugField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    
    def __str__(self):
        return self.username

class Category(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=125)
    content=models.CharField(max_length=250)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Tag(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=125)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=CASCADE)
    content=models.CharField(max_length=250)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content


class Post(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=125)
    content=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=CASCADE,blank=True,null=True)
    tags=models.ForeignKey(Tag, on_delete=CASCADE,blank=True,null=True)
    image=models.ImageField(upload_to='post',blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True,null=True)
    updated=models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return self.title
    



    