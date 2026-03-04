from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class ListView(generics.ListAPIView):
    """Retrieve all books (GET)."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author', 'publication_year']

class DetailView(generics.RetrieveAPIView):
    """Retrieve a single book by ID (GET)"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CreateView(generics.CreateAPIView):
    """Create a new book (POST)"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class UpdateView(generics.UpdateAPIView):
    """Update an existing book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
class DeleteView(generics.DestroyAPIView):
    """Remove a book (DELETE)"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
