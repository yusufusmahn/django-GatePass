from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



def index(request):
    return HttpResponse("Welcome to GatePass App")


def about(request):
    return render(request,template_name="about.html", context={"name": "yusuf"})