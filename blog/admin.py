from django.contrib import admin

from blog.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "is_published", "views_count")
    list_filter = ("is_published",)
    search_fields = ("title",)

    def link(self, obj):
        url = obj.get_absolute_url()
        return f'<a href="{url}" target="_blank">Смотреть</a>'

    link.short_description = "Ссылка на статью"
    link.allow_tags = True
