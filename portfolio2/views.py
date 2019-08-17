from django.shortcuts import render

def index (request):
    return render(request, 'portfolio2/portfolio2Page.html')
