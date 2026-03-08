from django.urls import path

from .views import UserLoginView, UserLogoutView, RegisterView, ProfileView, HomeView, create_post, PostListView

urlpatterns = [
        path('', HomeView.as_view(), name='home'),
        path('login/', UserLoginView.as_view(template_name='blog/login.html'), name='login'),
        path('logout/', UserLogoutView.as_view(template_name='blog/logout.html'), name='logout'),
        path('register/', RegisterView.as_view(), name='register'),
        path('profile/', ProfileView.as_view(), name='profile'),
        path('new/', create_post, name='create_posts'),
        path('posts/', PostListView.as_view(), name='posts'),
        path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
        path('<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
        path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
