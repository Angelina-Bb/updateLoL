from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Updates
from .models import *
# Login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

from AppLOL.forms import *

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def inicio(request):
    if request.user.is_authenticated:
        imagen_model = Avatar.objects.filter(user= request.user.id).order_by("-id")[0]
        imagen_url = imagen_model.imagen.url
    else:
        imagen_url = ""
    return render(request, "AppLOL/index.html", {"imagen_url": imagen_url})

def about(request):
    if request.user.is_authenticated:
        imagen_model = Avatar.objects.filter(user= request.user.id).order_by("-id")[0]
        imagen_url = imagen_model.imagen.url
    else:
        imagen_url = ""
    return render(request, "AppLOL/about.html", {"imagen_url": imagen_url})

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
    category = get_object_or_404(Category, slug=slug)

    return render(request, 'AppLOL/category.html', {'category': category})

def campeones(request):
    if request.user.is_authenticated:
        imagen_model = Avatar.objects.filter(user= request.user.id).order_by("-id")[0]
        imagen_url = imagen_model.imagen.url
    else:
        imagen_url = ""
    return render(request, "AppLOL/campeones.html", {"imagen_url": imagen_url})

def chat(request):
    if request.user.is_authenticated:
        imagen_model = Avatar.objects.filter(user= request.user.id).order_by("-id")[0]
        imagen_url = imagen_model.imagen.url
    else:
        imagen_url = ""
    return render(request, "AppLOL/chat.html", {"imagen_url": imagen_url})

def profile(request):
    if request.user.is_authenticated:
        imagen_model = Avatar.objects.filter(user= request.user.id).order_by("-id")[0]
        imagen_url = imagen_model.imagen.url
    else:
        imagen_url = ""
    return render(request, "AppLOL/profile.html", {"imagen_url": imagen_url})

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

@login_required
def agregar_avatar(request):
    
    if request.method == "POST":
        
        formulario = AvatarForm(request.POST, files=request.FILES)
        print(request.FILES, request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario = request.user

            avatar = Avatar(user=usuario, imagen=data["imagen"])
            avatar.save()

            return redirect("inicio")
        
        else:
            return render(request, "AppLOL/agregar_avatar.html", {"form": formulario, "errors": formulario.errors })
    
    formulario = AvatarForm()

    return render(request, "AppLOL/agregar_avatar.html", {"form": formulario})