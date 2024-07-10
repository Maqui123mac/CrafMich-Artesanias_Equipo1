from django.shortcuts import render, HttpResponse

# Create your views here.
def ca(request):
    return render(request, "michoacan/ca.html")
def bienvenida(request):
    return render(request, "michoacan/bienvenida.html")
