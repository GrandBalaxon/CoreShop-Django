from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from blog.models import BlogPost, Category


class BlogPostsView(ListView):
    model = BlogPost
    template_name = 'blog/home.html'
    context_object_name = 'blogposts'
    queryset = BlogPost.objects.filter(is_published=True)  # только опубликованные


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blog/blog_detail.html"
    context_object_name = "blogpost"

    def get_object(self, *args, **kwargs):
        blogpost = super().get_object(*args, **kwargs)
        if blogpost.is_published:
            blogpost.views_count += 1
            blogpost.save(update_fields=['views_count'])
            return blogpost
        else:
            return blogpost


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/write_blog.html'
    fields = ['title', 'category', 'content', 'preview']

    def get_context_data(self, **kwargs):
        context = {
            'categories': Category.objects.all(),
        }
        return context

    def form_valid(self, form):
        self.object = form.save()
        return render(self.request, "blog/blog_detail.html")
