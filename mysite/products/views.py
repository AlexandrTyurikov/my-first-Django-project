from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
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
