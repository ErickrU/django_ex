from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from datetime import date
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

def calculadora_años_plus(request, dia, mes, año, edad_futura):
    
    birthDate = date(año, mes, dia)
    today = date.today()
    age = edad_futura - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    message = f'Tu edad en el año {edad_futura} seria de: {age}\nUwU'
    return HttpResponse(message, content_type='text/pain; charset=utf-8')  

#render a page
def saludo_dinamico(request):
    paginaSaludo = open ('E:/django_ex/project_00/my_django_app/basics/templates/views/saludo_dinamico.html')
    plt =  Template(paginaSaludo.read())
    paginaSaludo.close()
    ctx = Context()
    docPagSaludo = plt.render(ctx)

    return HttpResponse(docPagSaludo)

#clase estudiante
class estudiante(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido =  apellido

def saludo_parametros(request):
    paginaSaludo = open ('E:/django_ex/project_00/my_django_app/basics/templates/views/parametros.html')

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

#f

    