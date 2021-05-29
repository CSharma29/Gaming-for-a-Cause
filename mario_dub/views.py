from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView
# Create your views here.

def home(request):
    return render(request, "mario_dub/home.html")
