from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="название")
    slug = models.SlugField(max_length=50, verbose_name="слаг")

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    description = models.TextField(verbose_name="описание")
    count = models.PositiveIntegerField(verbose_name="количество")
    price = models.PositiveIntegerField(verbose_name="цена")
    image = models.ImageField(verbose_name="фото")
    slug = models.SlugField(max_length=100, verbose_name="слаг")

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="категория"
    )

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def __str__(self):
        return self.name
