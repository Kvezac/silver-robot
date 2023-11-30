from datetime import date

from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Min, Max, Sum
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from mptt import utils
from mptt.exceptions import InvalidMove

from company.forms import AddEmployeeForm
from company.models import Employee
from company.utils import creat_paginator
from user.models import Profile


def home(request):
    title = 'Страница входа'
    context = {'title': title}
    return render(request, 'company/index.html', context)


@login_required
def main_employee(request):
    """
        The main page shows company statistics
    """
    title = 'Главная страница'
    levels = Employee.objects.all().count()
    managers = Employee.objects.exclude(parent=True).count()
    avg_subordinates = Employee.objects.aggregate(avg=Avg('children'))['avg']  # что-то не так
    unassigned_users = Profile.objects.filter(employee__isnull=True).count()

    stats = Employee.objects.aggregate(min_salary=Min('salary'), max_salary=Max('salary'), sum_salary=Sum('salary'),
                                       avg_salary=Avg('salary'))
    min_hire_date = Employee.objects.exclude(hire_date=None).aggregate(min=Min('hire_date'))['min']
    max_hire_date = Employee.objects.exclude(hire_date=None).aggregate(max=Max('hire_date'))['max']

    longest_employment = Employee.objects.filter(hire_date=min_hire_date).first()
    shortest_employment = Employee.objects.filter(hire_date=max_hire_date).first()

    from django.db.models import Count

    most_common_position = Employee.objects.values('position__name').annotate(count=Count('position')).order_by(
        '-count').first()
    least_common_position = Employee.objects.values('position__name').annotate(count=Count('position')).order_by(
        'count').first()

    context = {'title': title,
               'levels': levels,
               'managers': managers,
               'avg_subordinates': avg_subordinates,
               'unassigned_users': unassigned_users,
               'stats': stats,
               'longest_employment': longest_employment,
               'shortest_employment': shortest_employment,
               'least_common_position': least_common_position,
               'most_common_position': most_common_position,

               }

    return render(request, 'company/main_employee.html', context=context)


def list_employee_all(request):
    employees = Employee.objects.order_by('id')
    count_employees = len(employees)
    title = 'Все сотрудники'
    employees, paginator, custom_range = creat_paginator(request, employees)

    context = {
        'title': title,
        'count_employees': count_employees,
        'employees': employees,
        'paginator': paginator,
        'custom_range': custom_range
    }
    return render(request, 'company/list_employee_all.html', context)


def list_employee_id(request, level):
    nodes = Employee.objects.filter(level=level).order_by('id')
    count_nodes = len(nodes)
    title = f'Департамент уровень {level + 1}'
    nodes, paginator, custom_range = creat_paginator(request, nodes)
    context = {
        'title': title,
        'count_nodes': count_nodes,
        'nodes': nodes,
        'paginator': paginator,
        'custom_range': custom_range
    }
    return render(request, 'company/list_employee_id.html', context)


@login_required
def select_unassigned_users(request):
    unassigned_users = Profile.objects.filter(employee__isnull=True)
    count_unassigned_users = len(unassigned_users)
    title = 'Соискатели'
    unassigned_users, paginator, custom_range = creat_paginator(request, unassigned_users)
    context = {
        'title': title,
        'count_unassigned_users': count_unassigned_users,
        'unassigned_users': unassigned_users,
        'paginator': paginator,
        'custom_range': custom_range
    }
    return render(request, 'company/select_unassigned_users.html', context)


@login_required
def edit_employee(request, pk):
    employee = get_object_or_404(Employee, id=pk)
    title = f'Профиль: {employee}'
    context = {
        'title': title,
        'employee': employee,
    }
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()
            return redirect('user:profile', employee.id )
    else:
        form = AddEmployeeForm(instance=employee)
    context['form'] = form
    return render(request, 'company/edit_employee.html', context)


def search_results(request):
    search_query = request.GET.get('search_query') if request.GET.get('search_query') else ''
    employees = Employee.objects.distinct().filter(
        Q(name__user__last_name__istartswith=search_query[:1].upper()) |
        Q(name__last_name__icontains=search_query))  # .order_by('-name__last_name')
    print(employees)
    count_employees = len(employees)
    context = {'employees': employees,
               'search_query': search_query,
               'count_employees': count_employees}
    return render(request, 'company/list_employee_all.html', context)


@login_required
def add_employee(request, pk):
    profile = get_object_or_404(Profile, id=pk)
    title = f'Профиль: {profile}'
    context = {
        'title': title,
        'profile': profile,
    }
    employee, created = Employee.objects.get_or_create(name=profile)
    print(employee, created)
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.hire_date = date.today()
            employee.save()
            print('employee add')
            return redirect(
                'company:main-employee')
    else:
        form = AddEmployeeForm()
    context['form'] = form
    return render(request, 'company/add_employee.html', context)


def delete_employee(request, pk):
    user = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        user.node_delete()
        return redirect('company:main-employee')
    return render(request, 'block/delete_employee.html', {'user': user})
