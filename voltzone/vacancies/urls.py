import vacancies.views
from django.urls import path, re_path


urlpatterns = [
    path("", vacancies.views.vacancies_list, name="vacancies-list"),
    re_path(
        r"^(?P<vacancy_id>\d+)/$",
        vacancies.views.vacancy_detail,
        name="vacancy-detail",
    ),
]
