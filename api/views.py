from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters, exceptions

from users.permissions import IsAdminOrReadOnly
from .serializers import CategorySerializer, GenreSerializer, TitleSerializer
from .models import Category, Genre, Title
from .filters import TitlesFilter


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    http_method_names = ['get', 'post', 'delete']
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]

    def retrieve(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed('GET')


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().order_by('id')
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    http_method_names = ['get', 'post', 'delete']
    lookup_field = 'slug'

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]

    def retrieve(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed('GET')


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all().order_by('name')
    serializer_class = TitleSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filter_class = TitlesFilter
    filter_fields = ['category', 'genre', 'year', 'name']

    def perform_create(self, serializer):
        category = get_object_or_404(Category, slug=self.request.data.get('category'))
        genre = Genre.objects.filter(slug__in=self.request.data.getlist('genre'))
        serializer.save(category=category, genre=genre)

    def perform_update(self, serializer):
        category = get_object_or_404(Category, slug=self.request.data.get('category'))
        genre = Genre.objects.filter(slug__in=self.request.data.getlist('genre'))
        serializer.save(category=category, genre=genre)
