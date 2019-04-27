from django import forms
from django.forms import ModelForm
from .models import *


class SearchActiveForm(forms.Form):
    search = forms.CharField(label='Поиск', required=False)
    active = forms.BooleanField(label='', required=False)


class SearchForm(forms.Form):
    search = forms.CharField(label='Введите ключевое слово', required=False)


class AuthorCreateUpdateForm(ModelForm):
    class Meta:
        model = Author
        fields = (
            'active',
            'name',
            'description'
        )


class SeriesCreateUpdateForm(ModelForm):
    class Meta:
        model = Series
        fields = (
            'name',
            'description'
        )


class GenreCreateUpdateForm(ModelForm):
    class Meta:
        model = Genre
        fields = (
            'name',
            'description'
        )


class PublishingCreateUpdateForm(ModelForm):
    class Meta:
        model = Publishing
        fields = (
            'name',
            'description'
        )


class ProductsCreateUpdateForm(ModelForm):
    class Meta:
        model = Products
        fields = (
            'name',
            'image',
            'price',
            'author',
            'genre',
            'series',
            'publishing',
            'year',
            'pages',
            'binding',
            'format',
            'isbn',
            'weight',
            'age_limit',
            'sum',
            'active',
            'rating'
        )


# class AuthorUpdateForm(ModelForm):
#     class Meta:
#         model = Author
#         fields = (
#             'active',
#             'name',
#             'description'
#         )
#
#
# class SeriesUpdateForm(ModelForm):
#     class Meta:
#         model = Series
#         fields = (
#             'name',
#             'description'
#         )
#
#
# class GenreUpdateForm(ModelForm):
#     class Meta:
#         model = Genre
#         fields = (
#             'name',
#             'description'
#         )
#
#
# class PublishingUpdateForm(ModelForm):
#     class Meta:
#         model = Publishing
#         fields = (
#             'name',
#             'description'
#         )
#
#
# class ProductsUpdateForm(ModelForm):
#     class Meta:
#         model = Products
#         fields = (
#             'name',
#             'image',
#             'price',
#             'author',
#             'genre',
#             'series',
#             'publishing',
#             'year',
#             'pages',
#             'binding',
#             'format',
#             'isbn',
#             'weight',
#             'age_limit',
#             'sum',
#             'active',
#             'rating'
#         )
