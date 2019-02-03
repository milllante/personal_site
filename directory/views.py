from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from directory.models import Router

def download(requset,pk):
    file = str(Router.objects.get(pk=pk).specifications)

    file_path = os.path.join('', file)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    return HttpResponseNotFound('<h1>No Page Here</h1>')


