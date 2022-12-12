from django.urls import path
from AppLOL import views

urlpatterns = [
    path("", views.inicio),
    path("about/", views.about),
    path("actualizaciones/", views.updates),
    path("campeones/", views.campeones),
    path("comunidad/", views.comunidad),
    path("chat/", views.chat),
    path("login/", views.login_request),
]
