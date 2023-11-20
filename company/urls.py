from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('', views.home, name='home'),
    path('main-employee/', views.main_employee, name='main-employee'),
    path('list-employee-all/', views.list_employee_all, name='list-employee-all'),
    path('edit-employee/', views.edit_employee, name='edit-employee'),
    path('list-employee/<int:level>/', views.list_employee_id, name='list-employee-id'),
    path('search-results/', views.search_results, name='search-results'),

]
