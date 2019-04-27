from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView
from .models import *
from .forms import *


class SearchActiveLV(ListView):

    def get_queryset(self):
        qs = super().get_queryset()
        active = self.request.GET.get('active', False)  # живой
        search = self.request.GET.get('search', False)
        if active:
            qs = qs.filter(active=True)
        if search != 0:
            return qs.filter(name__contains=search)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchActiveForm()
        return context


class SearchLV(ListView):
    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('search', False)
        if search != 0:
            return qs.filter(name__contains=search)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm()
        return context


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


class AuthorList(SearchActiveLV):
    model = Author


class SeriesList(SearchLV):
    model = Series


class GenreList(SearchLV):
    model = Genre


class PublishingList(SearchLV):
    model = Publishing


class ProductsList(SearchActiveLV):
    model = Products


class AllHandbookView(TemplateView):
    template_name = 'products/all_handbook_view.html'


class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorCreateUpdateForm
    template_name = 'products/create_form.html'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('author_dv', kwargs={'pk': self.object.pk})
        return reverse_lazy('author_lv')


class SeriesCreate(CreateView):
    model = Series
    form_class = SeriesCreateUpdateForm
    template_name = 'products/create_form.html'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('series_dv', kwargs={'pk': self.object.pk})
        return reverse_lazy('series_lv')


class GenreCreate(CreateView):
    model = Genre
    form_class = GenreCreateUpdateForm
    template_name = 'products/create_form.html'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('genre_dv', kwargs={'pk': self.object.pk})
        return reverse_lazy('genre_lv')


class PublishingCreate(CreateView):
    model = Publishing
    form_class = PublishingCreateUpdateForm
    template_name = 'products/create_form.html'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('publishing_dv', kwargs={'pk': self.object.pk})
        return reverse_lazy('publishing_lv')


class ProductsCreate(CreateView):
    model = Products
    form_class = ProductsCreateUpdateForm
    template_name = 'products/create_form.html'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('book_dv', kwargs={'pk': self.object.pk})
        return reverse_lazy('book_lv')


class AuthorUpdate(UpdateView):
    model = Author
    form_class = AuthorCreateUpdateForm
    template_name = 'products/update_form.html'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('author_dv', kwargs={'pk': self.object.pk})
        return reverse_lazy('author_lv')


class SeriesUpdate(UpdateView):
    model = Series
    form_class = SeriesCreateUpdateForm
    template_name = 'products/update_form.html'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('series_dv', kwargs={'pk': self.object.pk})
        return reverse_lazy('series_lv')


class GenreUpdate(UpdateView):
    model = Genre
    form_class = GenreCreateUpdateForm
    template_name = 'products/update_form.html'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('genre_dv', kwargs={'pk': self.object.pk})
        return reverse_lazy('genre_lv')


class PublishingUpdate(UpdateView):
    model = Publishing
    form_class = PublishingCreateUpdateForm
    template_name = 'products/update_form.html'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('publishing_dv', kwargs={'pk': self.object.pk})
        return reverse_lazy('publishing_lv')


class ProductsUpdate(UpdateView):
    model = Products
    form_class = ProductsCreateUpdateForm
    template_name = 'products/update_form.html'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('book_dv', kwargs={'pk': self.object.pk})
        return reverse_lazy('book_lv')
