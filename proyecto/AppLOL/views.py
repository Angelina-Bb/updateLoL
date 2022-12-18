from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,JsonResponse

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
        try:
            imagen_model = Avatar.objects.filter(user= request.user.id).order_by("-id")[0]
            imagen_url = imagen_model.imagen.url
        except: 
            imagen_url = ""    
    else:
        imagen_url = ""
    return render(request, "AppLOL/index.html", {"imagen_url": imagen_url})

def about(request):
    if request.user.is_authenticated:
        try:
            imagen_model = Avatar.objects.filter(user= request.user.id).order_by("-id")[0]
            imagen_url = imagen_model.imagen.url
        except: 
            imagen_url = ""    
    else:
        imagen_url = ""
    return render(request, "AppLOL/about.html", {"imagen_url": imagen_url})

def updates(request):
    posts = Post.objects.all()
    if request.user.is_authenticated:
        try:
            imagen_model = Avatar.objects.filter(user= request.user.id).order_by("-id")[0]
            imagen_url = imagen_model.imagen.url
        except: 
            imagen_url = ""    
    else:
        imagen_url = ""
    return render(request,"AppLOL/actualizaciones.html", {'posts': posts, "imagen_url": imagen_url})

def detail(request, slug):
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

    if request.user.is_authenticated:
        try:
            imagen_model = Avatar.objects.filter(user= request.user.id).order_by("-id")[0]
            imagen_url = imagen_model.imagen.url
        except: 
            imagen_url = ""    
    else:
        imagen_url = ""

    return render(request,"AppLOL/detail.html", {'post': post, 'form': form, "imagen_url": imagen_url})

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)

    return render(request, 'AppLOL/category.html', {'category': category})

def profile(request):
    if request.user.is_authenticated:
        try:
            imagen_model = Avatar.objects.filter(user= request.user.id).order_by("-id")[0]
            imagen_url = imagen_model.imagen.url
        except: 
            imagen_url = ""    
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
    
    if request.user.is_authenticated:
        try:
            imagen_model = Avatar.objects.filter(user= request.user.id).order_by("-id")[0]
            imagen_url = imagen_model.imagen.url
        except: 
            imagen_url = ""    
    else:
        imagen_url = ""
    return render(request, "AppLOL/agregar_avatar.html", {"form": formulario, "imagen_url": imagen_url})

# views del chat

def home(request):
    return render(request, 'AppLOL/inicio_chat.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(room=room)
    return render(request, 'AppLol/chat.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(room=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(room=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Mensaje enviado')

def getMessages(request, room):
    room_details = Room.objects.get(room=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

# --------------------------