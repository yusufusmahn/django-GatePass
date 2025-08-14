from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



def index(request):
    return HttpResponse("Welcome to GatePass App")


def about(request):
    return HttpResponse("This App Is About Managing Visitors In An Estate")