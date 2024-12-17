# health/urls.py
from django.urls import path
from . import views
from .views import (
    CustomLoginView,
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView,
    UserRegistrationView,
    CustomLogoutView,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', UserRegistrationView.as_view(), name='register'),

    path('', views.home, name='home'),  # Add a default view to test the app

    # # Authentication paths
    # path('login/', auth_views.LoginView.as_view(template_name='health/login.html'), name='login'),
    # #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('register/', views.register, name='register'),
    # path('dashboard/', views.dashboard, name='dashboard'),  # Route for dashboard
    # path('logout/', views.user_logout, name='logout'),  # Route for logout
]
