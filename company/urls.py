from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('', views.home, name='home'),
    path('list-employee/', views.list_employee, name='list-employee'),
]
