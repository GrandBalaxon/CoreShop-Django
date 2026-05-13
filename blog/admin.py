from django.contrib import admin

from blog.models import BlogPost, Category


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "is_published", "views_count")
    list_filter = ("is_published",)
    search_fields = ("title",)


@admin.register(Category)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
