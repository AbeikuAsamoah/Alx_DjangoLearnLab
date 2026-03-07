from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

# Create your views here.

class UserLginView(LoginView):
    template_name = 'login.html'

class UserLogoutView(LogoutView):
    next_page = '/login/'

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
