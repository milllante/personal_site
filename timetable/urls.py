from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from timetable.models import Lessons

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Lessons.objects.all(), template_name='timetable/tablePage.html')),
]