from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ListView(generics.ListAPIView):
    """Retrieve all books (GET)."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class DetailView(generics.RetrieveAPIView):
    """Retrieve a single book by ID (GET)"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class CreateView(generics.CreateAPIView):
    """Create a new book (POST)"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class UpdateBook(generics.UpdateAPIView):
    """Update an existing book"""
    gueryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
class DeleteView(generics.DestroyAPIView):
    """Remove a book (DELETE)"""
    queryset = Book.objects.all()
    serializer_class = Book Serializer
    permission_classes = [IsAthenticated]
