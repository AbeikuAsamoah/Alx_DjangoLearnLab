from django.urls import path
from . import views

urlpatterns = [
        path('books/', views.list_all_books, name='book_list'),
        path('library/<int:pk>/', views.display_details.as_view(), name='library_books')
]
