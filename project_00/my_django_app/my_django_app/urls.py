"""my_django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from basics.views import saludar
from basics.views import adios
from basics.views import dameFecha
from basics.views import calculadora_años
from basics.views import saludo_dinamico
from basics.views import saludo_parametros
from basics.views import calculadora_años_plus
from basics.views import saludoShorCut
from basics.views import saludo_loader, carrera_tics, carrera_papalotes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludar),
    path('despedida/', adios),
    path('fecha/', dameFecha),
    path('edad/<int:año>/<int:edad>', calculadora_años),
    path('edadplus/<int:dia>/<int:mes>/<int:año>/<int:edad_futura>', calculadora_años_plus),
    path('holi/', saludo_dinamico),
    path('salu2/', saludo_parametros),
    path('salu3/', saludoShorCut),
    path('salu4/', saludo_loader),
    path('Tics/', carrera_tics),
    path('papalotes/', carrera_papalotes),

]
