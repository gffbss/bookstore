__author__ = 'geoffreyboss'

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    # author = models.OneToManyField(Author)

    def __unicode__(self):
        return self.name

class Genre(models.Model):
    genre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    book_list = models.CharField(max_length=100)