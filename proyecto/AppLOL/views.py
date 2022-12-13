from django.shortcuts import render, redirect
from django.http import HttpResponse

<<<<<<< HEAD
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
=======
# Updates
from .models import Post
# Login
from django.contrib.auth.forms import AuthenticationForm
>>>>>>> 83f22dd5e08b32bd89109d1104662923ee7a7d17
from django.contrib.auth import login, logout, authenticate

from AppLOL.forms import *

def inicio(request):
    return render(request,"AppLOL/index.html")

def about(request):
    return render(request,"AppLOL/about.html")

def updates(request):
<<<<<<< HEAD
    return render(request,"AppLOL/actualizaciones.html")

=======
    posts = Post.objects.all()

    return render(request,"AppLOL/actualizaciones.html", {'posts': posts})
>>>>>>> 83f22dd5e08b32bd89109d1104662923ee7a7d17
def campeones(request):
    return render(request,"AppLOL/campeones.html")

def comunidad(request):
    return render(request,"AppLOL/comunidad.html")

def chat(request):
    return render(request,"AppLOL/chat.html")

def register(request):
    return render(request,"AppLOL/register.html")

def profile(request):
    return render(request,"AppLOL/profile.html")

def login_request(request):
    
    errors = ""

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return render(request, {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, {"mensaje":f"Error, datos incorrectos."})
        else:
            return render(request, {"mensaje":f"Error, formulario erroneo"})
    form = AuthenticationForm()
    return render(request,'AppLOL/login.html' , {"form":form, "errors":errors})

def registrar_usuario(request):

    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
        else:
            return render(request, "AppLOL/register.html", {"form": formulario, "errors": formulario.errors})

    formulario = UserRegisterForm()
    return render(request,"AppLOL/register.html", {"form": formulario})
