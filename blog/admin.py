from django.contrib import admin

from blog.models import BlogPost, Category


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "is_published", "views_count", "link")
    list_filter = ("is_published",)
    search_fields = ("title",)

    def link(self, obj):
        url = obj.get_absolute_url()
        return f"http://127.0.0.1:8000{url}"

    link.short_description = "Ссылка на статью"
    link.allow_tags = True


@admin.register(Category)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
