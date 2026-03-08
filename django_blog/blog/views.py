from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, DetailView, UpdateView, DeleteView
from .forms import CustomUserCreationForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import Post


# Create your views here.

class UserLoginView(LoginView):
    template_name = 'login.html'

class UserLogoutView(LogoutView):
    next_page = '/login/'

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/profile.html'
    login_url = 'login'

class HomeView(TemplateView):
    template_name = 'blog/home.html'

def create_post(request):
    if request.method == "POST": 
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('posts')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})

class PostListView(ListView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'posts'
    ordering = ['-published_date']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post_details'

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy('posts')

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts')

