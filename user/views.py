from django.shortcuts import render

# Create your views here.

def user_list(request):
    context = User.objects.all()
    return render(request, 'user/user-list.html', context)
