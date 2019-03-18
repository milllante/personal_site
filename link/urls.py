from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from link.models import links

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=links.objects.all(), template_name='link/linkPage.html')),
]