from rest_framework import serializers
from .models import Book, BookNumber, BookCharacters, Authers

class BookNumberSerializer( serializers.ModelSerializer ) :
    class Meta:
        model = BookNumber
        fields = ("id", "isbn", "isbn13", )

class CharactersSerializer( serializers.ModelSerializer ) :
    class Meta:
        model = BookCharacters
        fields = ("id", "name", )

class AuthersSerializer( serializers.ModelSerializer ) :
    class Meta:
        model = Authers
        fields = ("id", "firstname", "lastname", )


class BookMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "title")

class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False)
    characters = CharactersSerializer(many=True)
    authers = AuthersSerializer(many=True)

    class Meta:
        model = Book
        fields = ("id", "title", "price", "number", "characters", "authers")
