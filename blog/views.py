from django.shortcuts import render, redirect
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

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not self.object.is_published:
            self.object.is_published = True
            self.object.save(update_fields=['is_published'])

        return redirect(self.object.get_absolute_url())


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


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/write_blog.html'
    fields = ['title', 'category', 'content', 'preview']
    context_object_name = 'blogpost'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        print(context)
        return context

    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.object.get_absolute_url())
