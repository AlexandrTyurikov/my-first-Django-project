"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from products.views import *

# from django.conf.urls.static import static
# from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('contacts', include('contacts.urls')),
    path('products/author/<int:pk>', AuthorDetail.as_view()),
    path('products/genre/<int:pk>', GenreDetail.as_view()),
    path('products/publishing/<int:pk>', PublishingDetail.as_view()),
    path('products/books/<int:pk>', ProductsDetail.as_view()),
    path('products/author/', AuthorList.as_view()),
    path('products/genre/', GenreList.as_view()),
    path('products/publishing/', PublishingList.as_view()),
    path('products/books/', ProductsList.as_view()),
]  # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
