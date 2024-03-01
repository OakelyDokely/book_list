from django.db import models
from django.db.models import Count

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50, verbose_name='Genre Name')
    def get_absolute_url(self):
        return "/genrelist"
    def __str__(self):
     return '{}'.format(self.name)

class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name='Author Name')
    nationality = models.CharField(max_length=50, verbose_name='Author Nationality')
    def get_absolute_url(self):
        return "/authorlist"
    def __str__(self):
        return '{}'.format(self.name)

class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name='Book Title')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Book Author')
    genre = models.ManyToManyField(Genre)
    def get_absolute_url(self):
        return "/booklist"
    def __str__(self):
        return '{}'.format(self.title)
