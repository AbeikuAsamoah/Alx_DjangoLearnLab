from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render
from .models import Post

# Create your views here.

class UserLginView(LoginView):
    template_name = 'login.html'

class UserLogoutView(LogoutView):
    next_page = '/login/'

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/profile.html'
    login_urls = 'login'

class HomeView(View):
    def get(self, request):
        return render(request, 'blog/home.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 5
