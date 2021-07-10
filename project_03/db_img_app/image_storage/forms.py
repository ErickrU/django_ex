from django import forms
from .models import *

class client_form(forms.ModelForm):
    class Meta:
        model = client
        fields = [
            'client_code',
            'enterprise',
            'first_name_client',
            'last_name_client',
            'position',
            'direction',
            'population',
            'telephone_number',
            'zip_code',
            'credit_card',
            'client_img_name',
            'client_img_img'
            ]
        labels = {
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
                'client_img_name': 'Nombre de la imagen',
                'client_img_img': 'Imagen'
            }

class products_form(forms.ModelForm):
    class Meta:
        model = products
        fields = [
            'product_code',
            'product_name',
            'description_product',
            'supplier_code',
            'unity_price',
            'unit_in_stock',
            'prodcuts_img_name',
            'prodcuts_img_img'
            ]
        labels = {
                'product_code': 'Codigo del producto',
                'product_name': 'Prodcuto',
                'description_product': 'Descripcion del producto',
                'supplier_code': 'Codigo de proveedor',
                'unity_price': 'Precio unitario',
                'unit_in_stock': 'Unidades en stock',
                'client_img_name': 'Nombre de la imagen',
                'prodcuts_img_img': 'Imagen'
            }

class order_form(forms.ModelForm):
    class Meta:
        model = order
        fields = [
            'order_code',
            'order_number',
            'client_code',
            'product_code'
            ]
        labels = {
                'order_code': 'Codigo del pedido',
                'order_number': 'Numero de pedido',
                'client_code': 'Codigo del cliente',
                'product_code': 'Codigo del producto'
            }
            