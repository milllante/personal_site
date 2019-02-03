from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from directory.models import Router
from . import views

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Router.objects.all(), template_name='directory/direct.html')),
    url(r'^(?P<pk>\d+)$', views.download, name='download'),
]