from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('profile/<pk>', views.user_profile, name='profile'),
    path('edit-profile/<pk>', views.edit_profile, name='edit-profile'),

]
