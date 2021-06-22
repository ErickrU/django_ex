from django import forms
from django.forms import fields
from .models import client, products, order

class client_form(forms.ModelForm):
    class Meta:
        model = client
        fields = ('client_code','enterprise','first_name_client','last_name_client','position','direction','population','telephone_number','zip_code','credit_card')
        labels = {
            'spanish': [{
                'client_code': 'Codigo del cliete',
                'enterprise': 'Empresa',
                'first_name_client': 'Nombres',
                'last_name_client': 'Apellidos',
                'position': 'Puesto',
                'direction': 'Direccion',
                'population': 'Poblacion',
                'telephone_number': 'Telefono',
                'zip_code': 'Codigo postal',
                'credit_card': 'Tarjeta de credito',
            }],
        }


class products_form(forms.ModelForm):
    class Meta:
        model = products
        fields = ('product_code','product_name','description_product','supplier_code','unity_price','unit_in_stock')
        labels = {
            'spanish': [{
                'product_code': 'Codigo del producto',
                'product_name': 'Nombre del producto',
                'description_product': 'Descripcion producto',
                'supplier_code': 'Codigo proveedor',
                'unity_price': 'Precio por unidad',
                'unit_in_stock': 'Unidades en existencia'
            }],
        }


class order_form(forms.ModelForm):
    class Meta:
        model = order
        fields = ('order_code','order_number','client_code','product_code')
        labels = {
            'spanish': [{
                'order_code': 'Codigo de pedido',
                'order_number': 'Numero de pedido',
                'client_code': 'Codigo del cliente',
                'product_code': 'Codigo producto',
            }],
        }
        


   