"""myblog URL Configuration

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
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('mainApp.urls')),
    url(r'^timetable/', include('timetable.urls')),
    url(r'^directory/', include('directory.urls')),
    url(r'^parents/', include('parents.urls')),
    url(r'^sites/', include('sites.urls')),
    url(r'^books/', include('books.urls')),
    url(r'^link/', include('link.urls')),
    url(r'^diploma/', include('diploma.urls')),
    url(r'^portfolio2/', include('portfolio2.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^portfolio/', include('portfolio.urls')),
]

