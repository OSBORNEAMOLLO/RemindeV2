# health/views.py
from django.http import HttpResponse
from django.contrib.auth.views import (LoginView, PasswordResetView, PasswordResetDoneView,
                                        PasswordResetConfirmView, PasswordResetCompleteView, LogoutView )
from .forms import CustomUserRegistrationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

#HOME PAGE
def home(request):

    context = {
        'title': 'Health Tracker'
    }
    return render(request, 'health/home.html', context)

# Login

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'  # For custom email templates
    success_url = '/password_reset/done/'  # Redirect after email is sent

    def form_valid(self, form):
        # Add custom logic for successful password reset requests
        return super().form_valid(form)
    

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = '/reset/done/'  # Redirect after password is successfully reset

    def form_valid(self, form):
        # Custom logic after password reset is successful
        return super().form_valid(form)
    
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'

class CustomLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'

class UserRegistrationView(CreateView):
    form_class = CustomUserRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')  # Redirect to login after registration





#USER REGISTRATION
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}! You can now log in.')
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'health/register.html', {'form': form})



# DASHBOARD
# @login_required
# def dashboard_view(request):
#     return render(request, 'dashboard.html')

# @login_required
# def dashboard(request):
#     return render(request, 'health/dashboard.html', {'user': request.user})

# def user_logout(request):
#     logout(request)
#     return redirect('login')  # Redirects to the login page after logout