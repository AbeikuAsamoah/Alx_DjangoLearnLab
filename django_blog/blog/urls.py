from django.urls import path

from .views import UserLoginView, UserLogoutView, RegisterView, ProfileView, HomeView, create_post, PostListView, PostDeleteView, PostUpdateView, PostDetailView, CommentCreateView, CommentDeleteView, CommentUpdateView

urlpatterns = [
        path('', HomeView.as_view(), name='home'),
        path('login/', UserLoginView.as_view(template_name='blog/login.html'), name='login'),
        path('logout/', UserLogoutView.as_view(template_name='blog/logout.html'), name='logout'),
        path('register/', RegisterView.as_view(), name='register'),
        path('profile/', ProfileView.as_view(), name='profile'),
        path('post/new/', create_post, name='create_posts'),
        path('post/', PostListView.as_view(), name='posts'),
        path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
        path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
        path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
        path('post/<int:post_id>/comment/new/', CommentCreateView.as_view(), name='add_comment'),
        path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit',),
        path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]
