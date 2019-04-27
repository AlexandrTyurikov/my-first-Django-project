from django.db import models
from django.urls import reverse_lazy


# from django.utils.safestring import mark_safe


class Author(models.Model):
    active = models.BooleanField('Автор жив', default=True)
    name = models.CharField('Автор(ы)', max_length=120)
    description = models.TextField('Автобиография', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('author_dv', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Series(models.Model):
    name = models.CharField('Серия', max_length=120)
    description = models.TextField('Описание', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('series_dv', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'


class Genre(models.Model):
    name = models.CharField('Жанр', max_length=120)
    description = models.TextField('Описание', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('genre_dv', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Publishing(models.Model):
    name = models.CharField('Издательство', max_length=120)
    description = models.CharField('Город', max_length=40)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('publishing_dv', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'


class Products(models.Model):
    name = models.CharField('Название книги', max_length=180)
    image = models.ImageField('Обложка', null=True, blank=True, upload_to='images')

    #    def image_tag(self):
    #        return mark_safe('<img src="/images/%s" width="150" height="150" />' % self.image)
    #    image_tag.short_description = 'Image'

    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    author = models.ManyToManyField('Author', related_name='products', verbose_name='Автор(ы)')
    genre = models.ManyToManyField('Genre', related_name='products', verbose_name='Жанр(ы)')
    series = models.ForeignKey('Series', null=True, blank=True, verbose_name='Серия', on_delete=models.PROTECT)
    publishing = models.ForeignKey('Publishing', verbose_name='Издательство', on_delete=models.PROTECT)
    year = models.IntegerField('Год издания')
    pages = models.IntegerField('Страниц')
    binding = models.CharField('Переплет', max_length=40)
    format = models.CharField('Формат', max_length=120)
    isbn = models.CharField('ISBN', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    age_limit = models.CharField('Возрастные ограничения', max_length=4)
    sum = models.IntegerField('Количество книг в наличии')
    active = models.BooleanField('Доступна для заказа', default=True)
    rating = models.DecimalField('Рейтинг', max_digits=2, decimal_places=1)
    creation_date = models.DateTimeField('Дата и время создания', auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField('Дата и время изменения', auto_now=True, auto_now_add=False)

    def get_absolute_url(self):
        return reverse_lazy('book_dv', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-name']
