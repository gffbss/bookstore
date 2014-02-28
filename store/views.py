__author__ = 'geoffreyboss'

from django.shortcuts import render, redirect
from store.models import Book, Author, Customer, Genre
from store.forms import BookForm

def home(request):
    return render(request, "home.html")

def books(request):
    library = Book.objects.all()
    return render(request, "library.html", {'library':library})

def new_books(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid:
            if form.save():
                return redirect("/books")

    else:
        form = BookForm()
    data = {'form':form}
    return render(request, "new_book.html", data)

#  Checkout the books
# def view_book(request, movie_id):
#     book = Book.objects.get(id=book_id)
#     data = {'book': book}
#     return render(request, "view_book.html", data)