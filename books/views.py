# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book, BookFilter, Author
from .serializers import BookSerializer, AuthorSerializer


def index(request):
    return HttpResponse('mic check')

def book_search(request):
    books = Book.objects.all()
    book_filter = BookFilter(request.GET, queryset=books)
    context = {'books': books, 'filter': book_filter}

    return render(request, 'books/search.html', context)

# def book_detail(request, book_id):
#   book = get_object_or_404(Book, pk=book_id)

#   return render(request, 'books/detail.html', {'book': book})

class BookDetail(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'

class AuthorDetail(generic.DetailView):
    model = Author
    template_name = 'books/author_detail.html'

@api_view(['GET', 'POST'])
def api_list(request, format=None):
    # list all books with GET... 
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    # ...or create book with POST
    elif request.method ==   'POST':
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print serializer.errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def api_detail(request, pk, format=None):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def author_api_list(request, format=None):
    # list all books with GET... 
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    # ...or create author with POST
    elif request.method ==   'POST':
        try:
            author = Author.objects.get(name__exact=request.data['name'])
            serializer = AuthorSerializer(data=request.data, instance=author)
        except Author.DoesNotExist:
            serializer = AuthorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print serializer.errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def author_api_detail(request, name, format=None):
    #update if author exists, else create new author
    try:
        author = Author.objects.get(name__exact=name)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AuthorSerializer(author)
        return Response(serializer.data)