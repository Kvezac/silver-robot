from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg, Min, Max, Sum
from django.shortcuts import render, get_object_or_404, redirect

from company.forms import EmployeeForms
from company.models import Employee


def home(request):
    title = 'Страница входа'
    context = {'title': title}
    return render(request, 'company/index.html', context)


# @login_required
def list_employee(request):
    """
        The main page shows company statistics
    """
    title = 'Главная страница'
    levels = Employee.objects.all().count()
    managers = Employee.objects.exclude(parent=True).count()
    avg_subordinates = Employee.objects.aggregate(avg=Avg('children'))['avg']
    stats = Employee.objects.aggregate(min_salary=Min('salary'), max_salary=Max('salary'), sum_salary=Sum('salary'),
                                       avg_salary=Avg('salary'))
    min_hire_date = Employee.objects.exclude(hire_date=None).aggregate(min=Min('hire_date'))['min']
    max_hire_date = Employee.objects.exclude(hire_date=None).aggregate(max=Max('hire_date'))['max']
    longest_employment = Employee.objects.filter(hire_date=min_hire_date).first()
    shortest_employment = Employee.objects.filter(hire_date=max_hire_date).first()
    context = {'title': title,
               'levels': levels,
               'managers': managers,
               'avg_subordinates': avg_subordinates,
               'stats': stats,
               'longest_employment': longest_employment,
               'shortest_employment': shortest_employment,

               }
    return render(request, 'company/list_employee.html', context=context)


def list_employee_all(request):
    nodes = Employee.objects.all()
    title = 'Все сотрудники'
    context = {
        'title': title,
        'nodes': nodes,
    }
    return render(request, 'company/list_employee_all.html', context)


def list_employee_id(request, level):
    nodes = Employee.objects.filter(level=level)
    title = f'Департамент уровнь {level}'
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


def list_employee_all(request):
    return None
