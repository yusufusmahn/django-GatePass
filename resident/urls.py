from django.urls import path
from . import views


urlpatterns = [
    path('add/house', views.add_house, name='add_house'),
    path('invite', views.create_invite, name='create_invite'),

]