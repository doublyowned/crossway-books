import q
from rest_framework import serializers
from models import Book, Author

class BookSerializer(serializers.ModelSerializer):

	class Meta:
		model = Book
		fields = ('id', 'title', 'category', 'medium', 'page_count', 'ISBN_10', 'pic_url', 'author')


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(read_only=False, many=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'pic_url', 'blurb', 'books')

    def create(self, validated_data):
        books_data = validated_data.pop('books')

        author = Author.object.get(name=validated_data['name'])

        for book_info in books_data:
            Book.objects.create(author=author, **book_info)

        return author

    def update(self, instance, validated_data):
        books_data = validated_data.pop('books')
        instance.name = validated_data.get('name', instance.name)
        instance.pic_url = validated_data.get('pic_url', instance.pic_url)
        instance.blurb = validated_data.get('blurb', instance.blurb)
        instance.save()

        for book_info in books_data:
            Book.objects.create(author=instance, **book_info)

        return instance

