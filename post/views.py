from django import views
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.views import View
from django.db import IntegrityError

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
class PostView(View):
    model=models.Post
    form_class=forms.PostForm
    template_name='post/post_form.html'
    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class})
    
    def post(self,request,*args,**kwargs):
        form=forms.PostForm(data=request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,'Post creado con exito')
                return redirect(to='list_post')
            except IntegrityError:
                messages.error(request,'No se pudo cargar el Post, intente nuevamente')
                return redirect(to='new_post')
        messages.error(request,'Algo a salido mal, por intenta nuevamente')
        return redirect(to='new_post')
