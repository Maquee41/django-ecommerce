import vacancies.views
from django.urls import path, re_path


app_name = "vacancies"

urlpatterns = [
    path("", vacancies.views.vacancies_list, name="list"),
    re_path(
        r"^(?P<vacancy_id>\d+)/$",
        vacancies.views.vacancy_detail,
        name="detail",
    ),
]
