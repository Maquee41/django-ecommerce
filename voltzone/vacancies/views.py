import django.shortcuts
from vacancies.models import Vacancy


def vacancies_list(request):
    vacancies = Vacancy.objects.filter(is_active=True)
    context = {
        "vacancies": vacancies,
    }
    return django.shortcuts.render(
        request, "vacancies/vacancies_list.html", context
    )


def vacancy_detail(request, vacancy_id):
    vacancy = django.shortcuts.get_object_or_404(Vacancy, pk=vacancy_id)
    context = {"vacancy": vacancy}
    return django.shortcuts.render(request, "vacancies/vacancy.html", context)
