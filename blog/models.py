from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(unique=True, max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="posts",
        verbose_name="Категория"
    )
    preview = models.ImageField(upload_to='images/blog/', null=True, blank=True, verbose_name="Превью")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    views_count = models.IntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        is_published = "Опубликовано" if self.is_published else "Не опубликовано"
        return f"{self.title} - {is_published} - Просмотров: {self.views_count}"

    def get_absolute_url(self):
        return reverse("blog:blog_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
