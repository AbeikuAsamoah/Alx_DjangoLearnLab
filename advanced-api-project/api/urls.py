from django.urls import path
from .views import ListView, DeleteView, UpdateView, CreateView, DetailView

urlpatterns = [
        path('books/', ListView.as_view(), name='book_list'),
        path('books/<int:pk>/', DetailView.as_view(), name='book_detail'),
        path('books/create/', CreateView.as_view(), name='create_book'),
        path('books/update/<int:pk>/', UpdateView.as_view(), name='update_book'),
        path('books/delete/<int:pk>/', DeleteView.as_view(), name='delete_book'),
]
