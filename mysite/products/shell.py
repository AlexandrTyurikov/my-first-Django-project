from products.models import *
from .models import *
# from products.shell import (выбрать функцию)


def create_author(obj):
    auth = Author(name=obj['name'])
    auth.save()
# create_author({'name':'Гогаль'})    - ввести в терминал


def create_genre(obj):
    gen = Genre(genre=obj['genre'])
    gen.save()
# create_genre({'genre':'Ужас'})    - ввести в терминал


def create_publishing(obj):
    publ = Publishing(publishing=obj['publishing'], city=obj['city'])
    publ.save()
# create_publishing({'publishing':'Альпина', 'city':'Москва'})    - ввести в терминал


def del_obj(ref, obj):
    ref.objects.get(pk=obj).delete()
# del_obj(Author, 3)    - ввести в терминал - удолит автора с pk=3


def count(ref):
    kol = ref.objects.count()
    print(kol)
# count(Genre)    - ввести в терминал - выдаст колличество жанров


# auth_list = []
# for i in range(1, 101):
#     obj = Author(name='new name ' + str(i))
#     auth_list.append(obj)
# Author.objects.bulk_create(auth_list)
