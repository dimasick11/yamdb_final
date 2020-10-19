from django.db import models


class Category(models.Model):
    name = models.CharField(null=False, blank=False, max_length=250)
    slug = models.SlugField(max_length=250, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(null=False, blank=False, max_length=250)
    slug = models.SlugField(max_length=250, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(null=False, blank=False, max_length=250)
    year = models.IntegerField(null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, blank=False, null=False, related_name='title'
    )
    genre = models.ManyToManyField(Genre, related_name='title_genre')

    def __str__(self):
        return self.name
