from django import forms
from django.forms import fields
from .models import alumno

class Alumno_form(forms.ModelForm):
    class Meta:
        model = alumno
        fields = ('nombre','apellido_paterno','apellido_materno','no_control','cuatrimestres','grupo')
        labels = {
            'nombre':'Nombre',
            'no_control':'Numero de control',
        }

    def __init__(self, *args, **kwargs):
        super(Alumno_form,self).__init__(*args, **kwargs)
        self.fields['grupo'].empty_label = 'Elije un grupo'
        self.fields['apellido_materno'].required = False