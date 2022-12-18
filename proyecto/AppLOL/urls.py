from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from AppLOL import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("about/", views.about, name="about"),
    path("actualizaciones/", views.updates, name="updates"),
    path("accounts/login/", views.login_request, name="login"),
    path("accounts/logout/", LogoutView.as_view(template_name="AppLol/logout.html"), name="logout"),
    path("accounts/signup/", views.registrar_usuario, name="register"),
    path("accounts/profile/", views.profile, name="profile"),
    path("accounts/profile/avatar/", views.agregar_avatar, name="agregar_avatar"),
    path("accounts/profile/editar/", views.editar_perfil, name="editar_perfil"),
    path("<slug:slug>/", views.detail, name = "post_detail"),
    path("chat/", views.home, name="home_chat"),
    path('<str:room>/', views.room, name='room'),
    path("checkview", views.checkview, name="checkview"),
    path("send", views.send, name="send"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
