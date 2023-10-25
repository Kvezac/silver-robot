from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

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
                login(request, user)
                return redirect('company:list-employee')

        return render(request, 'user/login.html', context)


def signup(request):
    title = "Регистрация в системе"
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
                return redirect('user:edit-profile')
        context['form'] = form
        return render(request, 'user/signup.html', context)


@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Вы вышли из системы")
        return redirect('company:home')


def user_profile(request):
    profile = request.user.profile
    employee = Employee.objects.get(name=profile.id)
    title = f'Профиль: {profile.name}'
    context = {
        'title': title,
        'profile': profile,
        'employee': employee,
    }
    return render(request, 'user/profile.html', context)


def edit_profile(request):
    profile = request.user.profile
    title = f'Страница редактирования: {profile.name}'
    forms = ProfileForm(instance=profile)
    if request.method == 'POST':
        forms = ProfileForm(request.POST, request.FILES, instance=profile)
        if forms.is_valid():
            forms.save()
            return redirect('user:profile')
    context = {'title': title,
               'forms': forms,
               }
    return render(request, 'user/edit_profile.html', context)
