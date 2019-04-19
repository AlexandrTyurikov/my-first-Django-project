from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import *


class AuthorDetail(DetailView):
    model = Author


class GenreDetail(DetailView):
    model = Genre


class PublishingDetail(DetailView):
    model = Publishing


class ProductsDetail(DetailView):
    model = Products


class AuthorList(ListView):
    model = Author


class GenreList(ListView):
    model = Genre


class ProductsList(ListView):
    model = Products


class PublishingList(ListView):
    model = Publishing
