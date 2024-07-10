from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .models import Articulos
from .form import LoginForm
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
def Carrusel(request):
    articulos=Articulos.objects.all()
    return render(request,"base/Carrusel.html", {'articulos':articulos})

def registro(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            # hacer algo después de guardar los datos del usuario
    else:
        form = LoginForm()
    return render(request, 'base/registro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('bienvenida')  
            HttpResponse('Ir a home')# Redirige a la página deseada después del login
                
    else:
        form = AuthenticationForm()
    return render(request, 'base/login.html', {'form': form})


class VRegistro(View):
    def post(self, request):
        form=UserCreationForm()
        return render(request, 'base/registro.html', {'form': form})
    

    def post(selft, request):
       form= UserCreationForm(request.POST)
       if form.is_valid():
            username =form.save()
            login(request,username)
            return redirect('home')
       else:
           pass
        
    

