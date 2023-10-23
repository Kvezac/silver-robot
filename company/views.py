from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from company.models import Employee


def home(request):
    title = 'main page'
    context = {'title': title}
    return render(request, 'company/index.html', context)


# @login_required
def list_employee(request):
    title = 'Все сотрудники'
    employees = Employee.objects.all()
    context = {'title': title,
               'employees': employees
               }
    return render(request, 'company/list_employee.html', context=context)


def list_employee_id(request, id):
    current_employee = Employee.objects.get(id=id)
    title = f'Лист сотрудников{current_employee.name.name}'
    root_employee_id = current_employee.get_root().id
    nodes = Employee.objects.all()
    context = {
        'title': title,
        'nodes': nodes,
        'current_employee': current_employee,
        'root_employee_id': root_employee_id
    }
    return render(request, 'company/list_employee_id.html', context)


def change_boss(request):
    return None
