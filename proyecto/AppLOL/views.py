from django.shortcuts import render
from django.http import HttpResponse

# Login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def inicio(request):
    return render(request,"AppLOL/index.html")
def about(request):
    return render(request,"AppLOL/about.html")
def updates(request):
    return render(request,"AppLOL/actualizaciones.html")
def campeones(request):
    return render(request,"AppLOL/campeones.html")
def comunidad(request):
    return render(request,"AppLOL/comunidad.html")
def chat(request):
    return render(request,"AppLOL/chat.html")

def login_request(request):
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
    return render(request,'AppLOL/index.html' , {"form":form})
