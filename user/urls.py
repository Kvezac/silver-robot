from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),

]
