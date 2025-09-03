from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"core/home.html")

def gallery(request):
    return render(request,"core/gallery.html")

def contacto(request):
    return render(request,"core/contacto.html")