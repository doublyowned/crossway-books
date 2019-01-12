from rest_framework import serializers
from models import Book

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ('id', 'title', 'category', 'medium', 'page_count', 'ISBN_10', 'pic_url', 'author')
