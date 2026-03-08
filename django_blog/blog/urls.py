from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, ProfileView, HomeView, PostListView

urlpatterns = [
        path('', HomeView.as_view(), name='home'),
        path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
        path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
        path('register/', RegisterView.as_view(), name='register'),
        path('profile/', ProfileView.as_view(), name='profile'),
        path('posts/', PostListView.as_view(), name='posts'),
]
