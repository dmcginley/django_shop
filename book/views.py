from django.views.generic import ListView, DetailView
from turtle import mode
from django.shortcuts import render
from .models import Book


def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'book/index.html', context)


class BookListView(ListView):
    model = Book
    template_name = 'book/index.html'

    context_object_name = 'books'
    # ordering = ['-date_posted']  # date posted in reverse order
    paginate_by = 24


class BookDetailView(DetailView):
    model = Book

# class BookListView(ListView):
#     mode = Book
#     template_name = 'book/books.html'
#     context_object_name = 'books'
#     paginate_by = 4
