from django import views
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.views import View
from . import forms

from . import models

class PostListView(ListView):
    model=models.Post

class PostDetailView(View):
    model=models.Post
    form_class=forms.PostForm
    template_name='post/post.html'
    def get(self,request,*args,**kwargs):
        post=get_object_or_404(models.Post,**kwargs)
        return render(request,self.template_name,{'post':post})