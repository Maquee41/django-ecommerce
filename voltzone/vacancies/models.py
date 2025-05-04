from django.db import models


class Vacancy(models.Model):
    title = models.CharField(max_length=100, verbose_name="название вакансии")
    short_description = models.TextField(
        max_length=100, verbose_name="краткое описание"
    )
    description = models.TextField(verbose_name="описание")
    is_active = models.BooleanField(default=True, verbose_name="активна")
    minimal_salary = models.PositiveIntegerField(
        verbose_name="зарплат от", null=True
    )
    created_at = models.DateTimeField(
        auto_now=True, verbose_name="дата создания"
    )

    class Meta:
        verbose_name = "вакансия"
        verbose_name_plural = "вакансии"

    def __str__(self):
        return self.title
