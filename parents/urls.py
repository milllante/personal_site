from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from parents.models import Parent

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Parent.objects.all(), template_name='parents/parentsPage.html')),
]