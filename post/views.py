from django import views
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
#from django.views import View
from django.views.generic import ListView


from . import models

class PostListView(ListView):
    model=models.Post


