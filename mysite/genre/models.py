from django.db import models


class Genre(models.Model):
    name = models.CharField('Название книги', max_length=120)
    genre = models.CharField('Жанр', max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
