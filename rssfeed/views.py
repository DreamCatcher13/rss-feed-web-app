from django.shortcuts import render
from django.http import HttpResponse
from .myHelpers import getFeeds

# Create your views here.
feeds = getFeeds()
c = {"feeds": feeds}
def index(request):
    return render(request, "index.html", context=c)