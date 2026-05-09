from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to='images/blog/', null=True, blank=True, verbose_name="Превью")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    views_count = models.IntegerField(verbose_name="Количество просмотров")

    def __str__(self):
        is_published = "Опубликовано" if self.is_published else "Не опубликовано"
        return f"{self.title} - {is_published} - Просмотров: {self.views_count}"

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
