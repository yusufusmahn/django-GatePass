from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


@api_view()
def create_resident(request):
    return Response("create resident")
