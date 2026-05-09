from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='images/catalog/', null=True, blank=True, verbose_name="Изображение")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="products"
    )
    price = models.IntegerField(verbose_name="Цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    def __str__(self):
        return f"{self.name}: ${self.price}"

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        ordering = ["price"]


class ContactInfo(models.Model):
    country = models.CharField(max_length=50, verbose_name="Страна", default="USA")
    TIN =  models.CharField(max_length=12, verbose_name="ИНН", default="91-1144442")
    address = models.CharField(max_length=300, verbose_name="Адрес", default="Redmond, WA, 98052-6399")

    def __str__(self):
        return f"{self.country} - {self.TIN} - {self.address}"

    class Meta:
        verbose_name = "контактная информация"
        verbose_name_plural = "контактная информация"
