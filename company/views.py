from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from company.models import Employee


def home(request):
    title = 'main page'
    context = {'title': title}
    return render(request, 'company/index.html', context)


# @login_required
def list_employee(request, id):
    title = 'Лист сотрудников'
    current_employee = Employee.objects.get(id=id)
    root_employee_id = current_employee.get_root().id
    nodes = Employee.objects.all()
    context = {
        'title': title,
        'nodes': nodes,
        'current_employee': current_employee,
        'root_employee_id': root_employee_id
    }
    return render(request, 'company/list_employee.html', context)


def change_boss(request):
    return None
