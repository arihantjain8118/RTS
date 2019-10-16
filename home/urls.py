from django.contrib import admin
from django.urls import path, include
from .views import starting,trains,ticketbook,ticketbk


urlpatterns = [
    path('', starting, name="home-home"),
    path('trains/',trains,name="home-trains"),
    path('book/<int:id>',ticketbook,name="home-book"),
    path('tickbk/',ticketbk,name="home-bk")
]