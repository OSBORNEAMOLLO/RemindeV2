from django.urls import path
from . import views

app_name = 'appointment'

urlpatterns = [
    path('', views.home, name='home'),
    # path('/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('<int:appointment_id>/', views.detail, name='detail'),
    path('dashboard/', views.index, name='index'),
    path('<int:consultation_id>/isdoctor/', views.isdoctor, name='isdoctor'),
    path('consultations/<str:filter_by>/', views.consultations, name='consultations'),
    path('create_appointment/', views.create_appointment, name='create_appointment'),
    path('<int:appointment_id>/create_consultation/', views.create_consultation, name='create_consultation'),
    path('<int:appointment_id>/delete_consultation/<int:consultation_id>/', views.delete_consultation, name='delete_consultation'),
    path('<int:appointment_id>/favorite_appointment/', views.favorite_appointment, name='favorite_appointment'),
    path('<int:appointment_id>/delete_appointment/', views.delete_appointment, name='delete_appointment'),
]
