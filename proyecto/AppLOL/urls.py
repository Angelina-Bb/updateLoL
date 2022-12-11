from django.urls import path
from AppLOL import views

urlpatterns = [
    path("", views.inicio) ,
    path("items/", views.items) ,
    path("campenes/", views.campeones) ,
]
