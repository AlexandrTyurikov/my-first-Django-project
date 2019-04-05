from django.db import models


class Author(models.Model):
    name = models.CharField('Название книги', max_length=120)
    name_a = models.CharField('Автор(ы)', max_length=140)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
