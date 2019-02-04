from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from books.models import Book
from . import views

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Book.objects.all(), template_name='books/booksPage.html')),
    url(r'^(?P<pk>\d+)$', views.download, name='download'),
]