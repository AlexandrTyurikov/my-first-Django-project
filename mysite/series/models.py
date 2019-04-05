from django.db import models


class Series(models.Model):
    name = models.CharField('Название книги', max_length=120)
    series = models.CharField('Серия', max_length=120)
    number = models.CharField('Номер', max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
