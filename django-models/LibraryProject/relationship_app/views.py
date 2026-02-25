from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

# Create your views here.

def list_all_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


class display_details(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['books']=self.object.books.all()

        return context
