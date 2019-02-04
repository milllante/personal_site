from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from sites.models import Site

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Site.objects.all(), template_name='sites/sitesPage.html')),
]