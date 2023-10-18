from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def home(request):
    title = 'main page'
    context = {'title': title}
    return render(request, 'company/index.html', context)


@login_required
def list_employee(request):
    title = 'Лист сотрудников'
    context = {'title': title}
    return render(request, 'company/list_employee.html', context)
