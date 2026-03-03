from .models import Book, Author
from rest_framework import serializers
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model that serializers all fields

    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """Ensure publication_year is not in the future"""
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication Year can't be in the future")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model
    Include a read-only list of books written by the author, using a nested BookSerializer.
    """
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['name', 'books']
