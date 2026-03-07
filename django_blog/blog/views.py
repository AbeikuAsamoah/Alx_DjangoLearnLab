from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class UserLginView(LoginView):
    template_name = 'login.html'

class UserLogoutView(LogoutView):
    next_page = '/login/'

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/profile.html'
    login_urls = 'login'
