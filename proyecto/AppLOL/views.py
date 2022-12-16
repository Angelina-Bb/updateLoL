from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Updates
from .models import *
# Login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from AppLOL.forms import *

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request,"AppLOL/index.html")

def about(request):
    return render(request,"AppLOL/about.html")

def updates(request):
    posts = Post.objects.all()

    return render(request,"AppLOL/actualizaciones.html", {'posts': posts})

def detail(request, category_slug, slug):
    posts = Post.objects.all()

    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()

    return render(request,"AppLOL/detail.html", {'posts': posts, 'form': form})

def category(request, slug):
    category = get_object_or_404

    return render(request, 'AppLOL/category.html', {'category': category})

def campeones(request):
    return render(request,"AppLOL/campeones.html")

def chat(request):
    return render(request,"AppLOL/chat.html")

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

@login_required
def editar_perfil(request):

    usuario = request.user

    if request.method == "POST":
        # cargar informacion en el formulario
        formulario = UserEditForm(request.POST)

        # validacion del formulario
        if formulario.is_valid():
            data = formulario.cleaned_data

            # actualizacion del usuario con los datos del formulario
            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]

            usuario.save()
            return redirect("inicio")
        else:
            return render(request, "AppLOL/editar_perfil.html", {"form": formulario, "erros": formulario.errors})
    else:
        # crear formulario vacio
        formulario = UserEditForm(initial = {"email": usuario.email})

    return render(request, "AppLOL/editar_perfil.html", {"form": formulario})
