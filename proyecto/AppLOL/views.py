from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse

# Updates
from .models import *
# Login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from AppLOL.forms import *


def inicio(request):
    return render(request,"AppLOL/index.html")

def about(request):
    return render(request,"AppLOL/about.html")

def updates(request):
    posts = Post.objects.all()

    return render(request,"AppLOL/actualizaciones.html", {'posts': posts})

def campeones(request):
    return render(request,"AppLOL/campeones.html")

def comunidad(request, slug):
    posts = Post.objects.all()

    post = get_list_or_404(Comunidad, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post

            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()

    return render(request,"AppLOL/comunidad.html", {'posts': posts, 'form': form})

def chat(request):
    return render(request,"AppLOL/chat.html")

def register(request):
    return render(request,"AppLOL/register.html")

def profile(request):
    return render(request,"AppLOL/profile.html")

def my_view(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
            print(user)
            if user is not None:
                login(request, user)
                return render(request, 'AppLOL/index.html', {"mensaje":f"Bienvenido {usuario}"})
        else:
            return render(request, 'AppLOL/login.html', {"form": form})
    form = AuthenticationForm()
    return render(request,'AppLOL/login.html' , {"form":form})


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

