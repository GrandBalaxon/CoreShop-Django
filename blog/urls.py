from django.urls import path
from . import views
from .apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path("", views.BlogPostsView.as_view(), name="blog"),
    path("post/<int:pk>/", views.BlogPostDetailView.as_view(), name="blog_detail"),
    path("post/new/", views.BlogPostCreateView.as_view(), name="blog_write"),
    path("post/<int:pk>/edit/", views.BlogPostUpdateView.as_view(), name="blog_edit"),
    path("post/<int:pk>/delete/", views.BlogPostDeleteView.as_view(), name="blog_delete"),
]