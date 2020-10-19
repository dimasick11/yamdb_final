from rest_framework import serializers

from .models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'slug']


class CategoryCheckField(serializers.SlugRelatedField):
    def to_representation(self, value):
        return CategorySerializer(value).data


class GenreCheckField(serializers.SlugRelatedField):
    def to_representation(self, value):
        return GenreSerializer(value).data


class TitleSerializer(serializers.ModelSerializer):
    category = CategoryCheckField(slug_field='slug', queryset=Category.objects.all(), required=False)
    genre = GenreCheckField(slug_field='slug', queryset=Genre.objects.all(), many=True)

    class Meta:
        model = Title
        fields = ['id', 'name', 'year', 'description', 'category', 'genre', 'rating']
