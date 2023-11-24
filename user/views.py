from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from company.models import Employee
from .forms import SigUpForm, SignInForm, ProfileForm
from .models import Profile


def login_user(request):
    title = "Вход в систему"
    context = {'title': title}
    if request.method == 'GET':
        form = SignInForm()
        context['form'] = form
        return render(request, 'user/login.html', context)
    elif request.method == "POST":
        form = SignInForm(request.POST)
        context['form'] = form
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                return redirect('user:edit-profile', user.id)

        return render(request, 'user/login.html', context)


def signup(request):
    title = "Регистрация"
    context = {'title': title}
    if request.method == 'GET':
        form = SigUpForm()
        context['form'] = form
        return render(request, 'user/signup.html', context)
    if request.method == 'POST':
        form = SigUpForm(request.POST)
        if form.is_valid():
            user_form = form.save()
            if user_form is not None:
                login(request, user_form)
                return redirect('user:edit-profile', request.user.id)
        context['form'] = form
        return render(request, 'user/signup.html', context)


@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('company:home')
    else:
        return redirect('user:login')


@login_required()
def delete_user(request, user_id):
    user = get_object_or_404(Profile, pk=user_id)
    if request.method == 'POST':
        print(user)
        user.delete()
        return redirect('company:main-employee')
    return render(request, 'block/delete_user.html', {'user': user})


@login_required
def user_profile(request, pk):
    profile = get_object_or_404(Profile, id=pk)
    title = f'Профиль: {profile.short_name()}'
    context = {
        'title': title,
        'profile': profile,
    }
    try:
        employee = Employee.objects.get(name=profile.id)
    except Employee.DoesNotExist:
        return render(request, 'user/profile.html', context)

    else:
        context['employee'] = employee
        return render(request, 'user/profile.html', context)


def edit_profile(request, pk):
    profile = get_object_or_404(Profile, id=pk)
    title = f'Редактирование: {profile.short_name()}'
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль обновлен')
            return redirect('user:profile', profile.id)
    context = {'title': title,
               'form': form,
               }
    messages.error(request, 'Что то пошло не так')
    return render(request, 'user/edit-profile.html', context)
