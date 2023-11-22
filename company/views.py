from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Min, Max, Sum
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from company.forms import EmployeeForms
from company.models import Employee
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
    return render(request, 'company/main_employee.html', context=context)


def list_employee_all(request):
    employees = Employee.objects.all()
    page = request.GET.get('page')
    result = 5
    title = 'Все сотрудники'
    paginator = Paginator(employees, result)
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        employees = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        employees = paginator.page(page)
    page = int(page)
    left_index = page - 2 if page > 2 else 1
    right_index = page + 3 if page < paginator.num_pages - 2 else paginator.num_pages + 1
    custom_range = range(left_index, right_index)

    context = {
        'title': title,
        'employees': employees,
        'paginator': paginator,
        'custom_range': custom_range
    }
    return render(request, 'company/list_employee_all.html', context)


def list_employee_id(request, level):
    nodes = Employee.objects.filter(level=level)
    title = f'Департамент уровень {level}'
    context = {
        'title': title,
        'nodes': nodes,
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


# @login_required
def select_unassigned_users(request):
    unassigned_users = Profile.objects.filter(employee__isnull=True)
    return render(request, 'company/select_unassigned_users.html', {'unassigned_users': unassigned_users})


def search_results(request):
    return None


def change_boss(request):
    return None


def add_employee(request, pk):
    profile = get_object_or_404(Profile, pk)
    print(profile)
    if request.method == 'POST':
        form = EmployeeForms(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()
            return render(request, 'block/success.html')
    else:
        form = EmployeeForms()
    return render(request, 'company/add_employee.html', {'form': form})


def select_level_and_boss(request):
    if request.method == 'POST':
        level = request.POST.get('level')
        boss = request.POST.get('boss')
        return render(request, 'company/select_position_salary.html', {'level': level, 'boss': boss})
    return render(request, 'company/select_level_and_boss.html')


def select_position_and_salary(request):
    if request.method == 'POST':
        position = request.POST.get('position')
        salary = request.POST.get('salary')
        return render(request, 'company/confirm_employee.html', {'position': position, 'salary': salary})
    return render(request, 'company/select_position_and_salary.html')


def create_employee(request):
    if request.method == 'POST' and request.is_ajax():
        level = request.POST.get('level')
        manager = request.POST.get('manager')
        position = request.POST.get('position')
        email = request.POST.get('email')
        salary = request.POST.get('salary')

        # Perform validation and create employee
        # ...

        return JsonResponse({'message': 'Employee created successfully'}, status=200)
    return JsonResponse({'error': 'Invalid request'}, status=400)