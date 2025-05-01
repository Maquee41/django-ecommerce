from django.db import models


class HomePage(models.Model):
    company_name = models.CharField(max_length=50, verbose_name="название")
    company_description = models.TextField(verbose_name="описание")

    class Meta:
        verbose_name = "главная страница"
