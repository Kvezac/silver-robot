from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SigUpForm, SignInForm


def login(request):
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
                return redirect('company:list-employee')
        context['form'] = form
        return render(request, 'user/signup.html', context)


@login_required
def logout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Вы вышли из системы")
        return redirect('company:home')
