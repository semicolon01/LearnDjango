from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# home page

def home(request):
    return HttpResponse("Hello Django!")

def api(request):
    data = {
        "1": {
            "title" : "hi1",
            "id" : 20,
            "slug" : "first-article"
        },
        "2": {
            "title": "hi2",
            "id": 21,
            "slug": "second-article"
        },
        "3": {
            "title": "hi3",
            "id": 22,
            "slug": "third-article"
        }
    }

    return JsonResponse(data)