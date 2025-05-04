from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from vacancies.models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(SummernoteModelAdmin):
    summernote_fields = ("description",)
