from django.urls import path
from . import views
from .apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path("", views.BlogPostsView.as_view(), name="blog"),
    path("post/<int:pk>/", views.BlogPostDetailView.as_view(), name="blog_detail"),
    path("post/new/", views.BlogPostCreateView.as_view(), name="blog_write"),
]