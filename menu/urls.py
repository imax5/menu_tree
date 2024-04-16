from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('products/', views.products, name='products'),
    path('users/', views.users, name='users'),
    path('all-users/', views.all_users, name='all_users'),
    path('all-users/add-user/', views.add_user, name='add_user'),
    path('all-users/add-user/add-user-single/', views.add_user_single, name='add_user_single'),
    path('all-users/add-user/add-user-file/', views.add_user_file, name='add_user_file'),

    path('other-menu/', views.other_menu, name='other_menu'),
]
