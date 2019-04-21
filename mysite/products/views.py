from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView, CreateView
from .models import *


class AuthorDetail(DetailView):
    model = Author


class SeriesDetail(DetailView):
    model = Series


class GenreDetail(DetailView):
    model = Genre


class PublishingDetail(DetailView):
    model = Publishing


class ProductsDetail(DetailView):
    model = Products


class AuthorList(ListView):
    model = Author


class SeriesList(ListView):
    model = Series


class GenreList(ListView):
    model = Genre


class ProductsList(ListView):
    model = Products


class PublishingList(ListView):
    model = Publishing


class AllHandbookView(TemplateView):
    template_name = 'products/all_handbook_view.html'


class AuthorCreate(CreateView):
    model = Author
    fields = ['name']
