from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
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

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('aaa', 0)
        if search != 0:
            return qs.filter(name__contains=search)
        return qs


class SeriesList(ListView):
    model = Series

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('sss', 0)
        if search != 0:
            return qs.filter(series__contains=search)
        return qs


class GenreList(ListView):
    model = Genre

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('ggg', 0)
        if search != 0:
            return qs.filter(genre__contains=search)
        return qs


class PublishingList(ListView):
    model = Publishing

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('ppp', 0)
        if search != 0:
            return qs.filter(publishing__contains=search)
        return qs


class ProductsList(ListView):
    model = Products

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('bbb', 0)
        if search != 0:
            return qs.filter(name__contains=search)
        return qs


class AllHandbookView(TemplateView):
    template_name = 'products/all_handbook_view.html'
