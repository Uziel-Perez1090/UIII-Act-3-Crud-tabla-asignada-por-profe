from django.shortcuts import render,redirect
from .models import clientes

def inicio_vista(request):
    losclientes=clientes.objects.all()
# Create your views here.
    return render(request,'gestionarClientes.html',{"misclientes":losclientes})



def registrarClientes(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos"]


    registrarClientes=clientes.objects.create(codigo=codigo,nombre=nombre,creditos=creditos)
    

    
    return redirect("/")

def seleccionarClientes(request,codigo):
    materia=clientes.objects.get(codigo=codigo)
    return render(request,"editarmateria.html",{"mismaterias":materia})


def editarClientes(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos"]


    materia=clientes.objects.get(codigo=codigo)
    materia.nombre=nombre
    materia.creditos=creditos
    materia.save()
    return redirect("/")


def borrarClientes(request,codigo):
    materia=clientes.objects.get(codigo=codigo)
    materia.delete()

    return redirect("/")
