from django.views.generic import ListView
from turtle import mode
from django.shortcuts import render
from .models import Book


def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'book/index.html', context)


def all_books(request):

    books = Book.objects.all()

    context = {
        'books': books,
    }
    return render(request, 'book/books.html', context)


# class BookListView(ListView):
#     mode = Book
#     template_name = 'book/books.html'
#     context_object_name = 'books'
#     paginate_by = 4
