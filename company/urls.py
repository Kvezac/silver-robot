from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('', views.home, name='home'),
    path('list-employee/<int:id>/', views.list_employee, name='list-employee'),
    path('change_boss/', views.change_boss, name='change_boss'),
]
