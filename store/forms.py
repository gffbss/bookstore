__author__ = 'geoffreyboss'

from django.forms import ModelForm
from store.models import Book, Author, Genre, Customer


class BookForm(ModelForm):
    class Meta:
        model = Book