from django.shortcuts import render
from django.http import HttpResponse


# home page

def home(request):
    return HttpResponse("Hello Django!")
