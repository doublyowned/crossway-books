from rest_framework import serializers
from models import Book, Author

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ('id', 'title', 'category', 'medium', 'page_count', 'ISBN_10', 'pic_url', 'author')

class AuthorWorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'pic_url')

class AuthorSerializer(serializers.ModelSerializer):
    books = AuthorWorksSerializer(many=True, read_only=True)
    id = serializers.ReadOnlyField()

    class Meta:
        model = Author
        fields = ('id', 'name', 'pic_url', 'blurb', 'books')