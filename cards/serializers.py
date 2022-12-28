from rest_framework import serializers
from .views import Type, Genre, Card, Review
from author.serializers import RegisterSerializer


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    author = RegisterSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'author', 'text', 'cards')
        read_only_fields = ('id', 'author', 'cards')


class ReviewCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = 'id author text cards'.split()
        read_only_fields = "id cards".split()

