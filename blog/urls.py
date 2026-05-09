from django.urls import path
from . import views
from .apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path("", views.BlogPostsView.as_view(), name="blog"),
]