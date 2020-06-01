from django.contrib import admin
from django.urls import path, include
from .views import starting,ticketbook,ticketbk,realbook,ticket,tickt,canceltic,pnrstatus,about,payment,booking,search,ticketbook2,ticketbk2,realbook2


urlpatterns = [
    path('', starting, name="home-home"),
    path('about/', about, name="about"),
    path('book/<int:id>/<str:date>/',ticketbook,name="home-book"),
    path('book2/<int:id1>/<int:id2>/<str:date>/',ticketbook2,name="home-book2"),
    path('book/<int:id>/<str:date>/form/',ticketbk,name="home-bookform"),
    path('book2/<int:id1>/<int:id2>/<str:date>/form/',ticketbk2,name="home-bookform2"),
    path('tickbk/',ticketbk,name="home-bk"),
    path('book/<int:id>/<str:date>/form/realbook/',realbook,name="home-realbook"),
    path('book2/<int:id1>/<int:id2>/<str:date>/form/realbook/',realbook2,name="home-realbook2"),
    path('ticket/<str:pnr>/',tickt,name="tickt"),
    path('canceltic/<str:pnr>/',canceltic,name="home-cantic"),
    path('pnrstatus',pnrstatus,name="pnrstatus"),
    path('payment/', payment, name='payment'),
    path('booking/', booking, name='booking'),
    path('search/<str:source>/<str:destination>/<str:date>/', search, name='search'),
]