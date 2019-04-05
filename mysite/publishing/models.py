from django.db import models


class Publishing(models.Model):
    name = models.CharField('Название книги', max_length=120)
    year = models.CharField('Год издания', max_length=4)
    city = models.CharField('Город', max_length=40)
    who = models.CharField('Издательство', max_length=140)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
