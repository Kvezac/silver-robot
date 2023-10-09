from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'company/home.html', context)
