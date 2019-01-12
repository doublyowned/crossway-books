# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from books.models import Book
from books.serializers import BookSerializer


def index(request):
	return HttpResponse('mic check')

@api_view(['GET', 'POST'])
def book_list(request, format=None):
	# list all books with GET... 
	if request.method == 'GET':
		books = Book.objects.all()
		serializer = BookSerializer(books, many=True)
		return Response(serializer.data)

	# ...or create book with POST
	elif request.method ==	 'POST':
		serializer = BookSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def book_detail(request, pk, format=None):
	try:
		book = Book.objects.get(pk=pk)
	except Book.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = BookSerializer(book)
		return Response(serializer.data)