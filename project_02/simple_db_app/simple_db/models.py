from django.db import models
from django.core.validators import MaxValueValidator
from django.db.models.manager import Manager

# Create your models here.

class client(models.Model):
    client_code = models.BigIntegerField(primary_key=True, validators=[MaxValueValidator(9999999999)])
    enterprise = models.CharField(max_length=100)
    first_name_client = models.CharField(max_length=100)
    last_name_client = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    direction = models.CharField(max_length=200)
    population = models.BigIntegerField()
    telephone_number = models.BigIntegerField(validators=[MaxValueValidator(9999999999)])
    zip_code = models.BigIntegerField(validators=[MaxValueValidator(99999)])
    credit_card = models.BigIntegerField(validators=[MaxValueValidator(9999999999999999)])
    def __str__(self):
        return str(self.client_code)

class products(models.Model):
    product_code = models.BigIntegerField(primary_key=True, validators=[MaxValueValidator(9999999999)])
    product_name = models.CharField(max_length=150)
    description_product = models.CharField(max_length=300)
    supplier_code = models.BigIntegerField(validators=[MaxValueValidator(9999999999)])
    unity_price = models.BigIntegerField()
    unit_in_stock = models.BigIntegerField()
    def __str__(self): #se usa esto para poder pasar esto como str y no como object y str() para no pasar int 
        return str(self.product_code)

class order(models.Model):
    order_code = models.BigIntegerField(primary_key=True, validators=[MaxValueValidator(9999999999)])
    order_number = models.BigIntegerField()
    client_code = models.ForeignKey(client, on_delete=models.PROTECT)
    product_code = models.ForeignKey(products, on_delete=models.PROTECT)