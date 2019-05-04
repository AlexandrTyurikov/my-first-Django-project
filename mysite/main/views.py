from django.views.generic import ListView
from book.models import Book
from django.db.models import Q


class BookCard(ListView):
    model = Book
    template_name = 'main/mainPage.html'

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('nnn', False)
        # list_book_pk = []
        if search != 0:
            return qs.filter(Q(name__icontains=search))  # | (Q(author__icontains=search))
        # elif self.request.GET.get('aaa', False):
        #     return qs.filter(Q(author__icontains=list_book_pk))
        return qs
