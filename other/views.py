from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def other_view(request):
    return HttpResponse("Welcome to brain project!")
