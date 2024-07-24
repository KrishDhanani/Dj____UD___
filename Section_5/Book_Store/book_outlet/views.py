from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Book

# Create your views here.

def index(request):
    books = Book.objects.all()      # From database try to getting all books
    return render(request, 'book_outlet/index.html',{
        "books": books,
    })

def book_detail(request, id):    # we set name here parameter to id because in urls.py file we set there "id" so need to use same name here.
    # try:
    #     book = Book.objects.get(pk=id)
    #     # here "pk" means primary key; you can also write id=id.
    # except: 
    #     raise Http404()

    # Ulternatively of upper code
    book = get_object_or_404(Book, pk=id)
    return render(request, 'book_outlet/book_detail.html',{
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling": book.is_bestselling,
        })
