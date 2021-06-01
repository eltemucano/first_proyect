from django.shortcuts import HttpResponse, redirect # agrega redirección a la declaración de importación
from django.http import JsonResponse

# En esta sección defines las vistas y lo que devuelve
def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")


def new(request):
    return  HttpResponse("Placeholder para mostrar un nuevo formulario para crear un nuevo blog")


def create(request):
    return HttpResponse("Acá creo algo?... ni idea")


def show(request, my_val):
    return HttpResponse(f"Placeholder para mostrar el blog numero : {my_val}")


def edit(request, my_val):
    return HttpResponse(f"Placeholder para editar el blog numero : {my_val}")


def destroy(request, my_val):
    return HttpResponse(f"Placeholder para eliminar el blog numero : {my_val}")


def jsonView(request):
    return JsonResponse({"key": 1})


def redirige(request):
    return redirect("/blogs") # Nota mental : Que no se te olvide mermelada de ... 
