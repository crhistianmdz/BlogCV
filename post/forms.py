from django.db.models import fields
from . import models
from django import forms

class CategoryForm(forms.ModelForm):
    title=fields.CharField(max_length=100)
    slug=fields.SlugField(max_length=125)
    content=fields.CharField(max_length=250)
    class Meta:
        model=models.Category
        fields='__all__'


class TagsForm(forms.ModelForm):
    class Meta:
        model=models.Tag
        fields='__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model=models.Comment
        fields=['user','content']

class PostForm(forms.ModelForm):
    class Meta:
        model=models.Post
        fields='__all__'