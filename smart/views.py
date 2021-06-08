import requestsp
from django.shortcuts import render
from django.shortcuts import HttpResponse
from bs4 import BeautifulSoup

# Create your views here.

def home(request):
    return render (request, 'base.html')


def searchthink(request):
    mysearch= request.POST.get('searchthink')
    mysearch1={'searchthink':mysearch}
    return render (request, 'my_web/new_search.html', mysearch1)
