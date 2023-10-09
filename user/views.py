from django.shortcuts import render
from .models import User


def user_list(request):
    context = User.objects.all()
    return render(request, 'user/user-list.html', context)
