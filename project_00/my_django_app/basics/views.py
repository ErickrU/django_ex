from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
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

    ahora = datetime.datetime.now()
    arreglo_2 = ["valor_1","Valor_2","Valor_3"]
    arreglo_3 = ['0','1','2','3','4','5','6','7','8','9','10',]
    estudiante1 = estudiante('margarita', 'lopez')
    #crea templates
    plt =  Template(paginaSaludo.read())
    #cerra
    paginaSaludo.close()
    #crear contexto 
    ctx = Context({'nombre_estudiante': estudiante1.nombre, 'apellido_estudiante': estudiante1.apellido, "arreglo_1":['Elemento1','Elemento2'], "arreglo_2":arreglo_2, "arreglo_3":arreglo_3, "fecha":ahora})
    #reder plant
    docPagSaludo = plt.render(ctx)
    return HttpResponse(docPagSaludo)

def saludoShorCut(request):

    ahora = datetime.datetime.now()
    arreglo_2 = ["valor_1","Valor_2","Valor_3"]
    arreglo_3 = ['0','1','2','3','4','5','6','7','8','9','10',]

    estudiante1 = estudiante ('yuya','algo')

    return render(request, "parametros.html",{'nombre_estudiante': estudiante1.nombre, 'apellido_estudiante': estudiante1.apellido, "arreglo_1":['Elemento1','Elemento2'], "arreglo_2":arreglo_2, "arreglo_3":arreglo_3, "fecha":ahora})

#loader

def saludo_loader(request):
    #paginaSaludo = open ('E:/django_ex/project_00/my_django_app/basics/templates/views/parametros.html')

    ahora = datetime.datetime.now()
    arreglo_2 = ["valor_1","Valor_2","Valor_3"]
    arreglo_3 = ['0','1','2','3','4','5','6','7','8','9','10',]
    estudiante1 = estudiante('yo', 'fui')
    #crea templates
    #plt =  Template(paginaSaludo.read())
    #cerra
    pagina_loader = loader.get_template("parametros.html")
    #paginaSaludo.close()
    #crear contexto 
    #ctx = Context({'nombre_estudiante': estudiante1.nombre, 'apellido_estudiante': estudiante1.apellido, "arreglo_1":['Elemento1','Elemento2'], "arreglo_2":arreglo_2, "arreglo_3":arreglo_3, "fecha":ahora})
    #reder plant
    docPagSaludo = pagina_loader.render({'nombre_estudiante': estudiante1.nombre, 'apellido_estudiante': estudiante1.apellido, "arreglo_1":['Elemento1','Elemento2'], "arreglo_2":arreglo_2, "arreglo_3":arreglo_3, "fecha":ahora})
    return HttpResponse(docPagSaludo)

#herencia
def carrera_tics(request):
    correo_tics = "fmwemfie@algo.com"

    return render(request, "child1.html", {"correo_tics":correo_tics})

def carrera_papalotes(request):
    correo_gpi = "pepe@papalotes.edu.mx"

    return render(request, "child2.html", {"correo_papalotes":correo_gpi})