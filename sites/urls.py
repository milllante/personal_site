from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from sites.models import Sites

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Sites.objects.all(), template_name='sites/sitesPage.html')),
]
