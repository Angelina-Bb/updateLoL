from django.shortcuts import render
from django.http import HttpResponse

# Login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def inicio(request):
    return render(request,"AppLOL/index.html")
def items(request):
    return HttpResponse("Los cambios de los items")
def campeones(request):
    return HttpResponse("Buffeos y Nerfeos")

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
