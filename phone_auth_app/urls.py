from django.urls import path
from . import views

urlpatterns = [
    path('auth/phone/', views.auth_phone, name='auth_phone'),
    path('auth/code/', views.auth_code, name='auth_code'),
    path('user/profile/', views.user_profile, name='user_profile'),
    path('activate/invite/', views.activate_invite, name='activate_invite'),
    path('invited/users/', views.invited_users, name='invited_users'),
]