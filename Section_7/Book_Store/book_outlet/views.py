from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Book
from django.db.models import Avg, Max, Min

# Create your views here.

def index(request):
    books = Book.objects.all().order_by("-title")      
    # From database try to getting all books in order by title.(It is ascending order, for descending order simpaly do '-' as upper shown.)
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))  # You can passnumber of aggregation here as many you like  

    return render(request, 'book_outlet/index.html',{
        "books": books,
        "total_number_of_books": num_books,
        "average_rating": avg_rating,
    })

def book_detail(request, slug):    # before we set name here parameter to id because in urls.py file we set there "id" so need to use same name here.
    #  But now change to slug so use here slug.
    # try:
    #     book = Book.objects.get(pk=id)
    #     # here "pk" means primary key; you can also write id=id.
    # except: 
    #     raise Http404()

    # Ulternatively of upper code
    book = get_object_or_404(Book, slug=slug)   # we set pk=id before slug=slug
    return render(request, 'book_outlet/book_detail.html',{
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling": book.is_bestselling,
        })
