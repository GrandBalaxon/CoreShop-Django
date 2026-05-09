from django.shortcuts import render
from django.views.generic import ListView

from blog.models import BlogPost


class BlogPostsView(ListView):
    model = BlogPost
    template_name = 'blog/home.html'
    context_object_name = 'blogposts'
