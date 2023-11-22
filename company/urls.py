from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('list-employee/<int:level>/', views.list_employee_id, name='list-employee-id'),
    path('add-employee/<pk>/', views.add_employee, name='add-employee'),
    path('main-employee/', views.main_employee, name='main-employee'),
    path('list-employee-all/', views.list_employee_all, name='list-employee-all'),
    path('edit-employee/', views.edit_employee, name='edit-employee'),
    path('search-results/', views.search_results, name='search-results'),
    path('unassigned-users/', views.select_unassigned_users, name='unassigned-users'),
    path('', views.home, name='home'),


    path('creat-employee', views.create_employee, name='creat-employee')

]
