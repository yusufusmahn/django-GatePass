from django.urls import path
from . import views

urlpatterns = [
    path("home", views.index),
    path("about", views.about),

]
#http://localhost:8000/demo/home
#python manage.py runserver