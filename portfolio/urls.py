from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from portfolio.models import Portfolio

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Portfolio.objects.all(), template_name='portfolio/portfolioPage.html')),
]