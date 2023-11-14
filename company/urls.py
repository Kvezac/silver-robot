from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('', views.home, name='home'),
    path('list-employee/', views.list_employee, name='list-employee'),
    path('edit-employee/', views.edit_employee, name='edit-employee'),
    path('list-employee/<int:level>/', views.list_employee_id, name='list-employee-id'),
]
