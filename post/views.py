from django import views
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import ListView, DeleteView
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
    def get(self,request,**kwargs):
        post=get_object_or_404(models.Post,**kwargs)
        return render(request,self.template_name,{'post':post})

class PostNewView(View):
    model=models.Post
    form_class=forms.PostForm
    template_name='post/post_form.html'
    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class})
    
    def post(self,request):
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

class PostUpdateViews(View):
    model=models.Post
    template_name='post/post_form.html'
    form_class=forms.PostForm
    def get(self,request,**kwargs):
        post=get_object_or_404(models.Post,**kwargs)
        form=self.form_class(instance=post)
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        post=get_object_or_404(models.Post,slug=request.POST['slug'])
        form=self.form_class(data=request.POST,instance=post)
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

class PostDeleteView(DeleteView):
    model=models.Post
    success_url='/'
    def post(self,request):
        messages.success(request,'post eliminada con exito')
    