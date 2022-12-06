from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def greeting(request):
    greeting = "Hi She'Neaker Heads"
    return HttpResponse(greeting)
