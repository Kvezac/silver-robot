from django.shortcuts import render


def login(request):
    title = "Вход в систему"
    context = {'title': title}
    return render(request, 'user/login.html', context)


def signup(request):
    title = "Регистрация в систему"
    context = {'title': title}
    return render(request, 'user/signup.html', context)