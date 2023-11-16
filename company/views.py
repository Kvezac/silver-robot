from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from company.forms import EmployeeForms
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


def list_employee_id(request, level):
    nodes = Employee.objects.filter(level=level)
    title = f'Лист сотрудников департамента уровня {level}'
    # root_employee_id = current_employee.get_level()
    # print(root_employee_id)
    # nodes = Employee.objects.all()
    # nodes = current_employee.get_descendant() #.filter(level__gte=root_employee_id)
    context = {
        'title': title,
        'nodes': nodes,
        # 'current_employee': current_employee,
        # 'root_employee_id': root_employee_id
    }
    return render(request, 'company/list_employee_id.html', context)


def edit_employee(request):
    if request.method == 'POST':
        form = EmployeeForms(request.POST, instance=request.user.profile.employee_set.all().first())
        if form.is_valid():
            employee = form.save(commit=False)
            if employee.get_parent == request.user.profile.employee_set.all().first():
                employee.save()
                return redirect('user:profile')
            else:
                return redirect('user:profile')
    else:
        form = EmployeeForms(instance=request.user.profile.employee_set.all().first())
    return render(request, 'company/edit_employee.html', {'form': form})


def search_results(request):
    return None


def change_boss(request):
    return None