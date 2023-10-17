from django.shortcuts import render


def home(request):
    title = 'main page'
    context = {'title': title}
    return render(request, 'company/index.html', context)
