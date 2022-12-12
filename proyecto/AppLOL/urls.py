from django.urls import path
from AppLOL import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("about/", views.about, name="about"),
    path("actualizaciones/", views.updates, name="updates"),
    path("campeones/", views.campeones, name="campeones"),
    path("comunidad/", views.comunidad, name="comunidad"),
    path("chat/", views.chat, name="chat"),
    path("accounts/login/", views.login_request, name="login"),
    path("accounts/register/", views.register, name="register"),
    path("accounts/profile/", views.profile, name="profile"),
]
