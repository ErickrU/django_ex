from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
import datetime 

# Create your views here.

def saludar(request):
    return HttpResponse('holi')

def adios(request):
    return HttpResponse('adios')

def dameFecha(request):

    ahora = datetime.datetime.now()
    msg = f'tomando clases {ahora}'
    return HttpResponse(msg)

def calculadora_años(request, año, edad):
    edadActual = edad
    now =  datetime.datetime.now().year
    print(now)
    periodo = año-now
    edadPost = edadActual + periodo
    message = f'En el año {año} tendras {edadPost}'
    return HttpResponse(message, content_type='text/pain; charset=utf-8') 

#clase estudiante
class estudiante(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido =  apellido

#render a page
def saludo_simple(request):
    paginaSaludo = open ('C:/Users/RTS/Documents/project_02/my_django_app/basics/templates/views/parametros.html')

    estudiante1 = estudiante('margarita', 'lopez')
    #crea templates
    plt =  Template(paginaSaludo.read())
    #cerra
    paginaSaludo.close()
    #crear contexto
    ctx = Context({'nombre_estudiante': estudiante1.nombre, 'apellido_estudiante': estudiante1.apellido})
    #reder plant
    docPagSaludo = plt.render(ctx)
    return HttpResponse(docPagSaludo)


    