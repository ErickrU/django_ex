# Generated by Django 3.2.4 on 2021-06-21 09:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('client_code', models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('enterprise', models.CharField(max_length=100)),
                ('first_name_client', models.CharField(max_length=100)),
                ('last_name_client', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('direction', models.CharField(max_length=200)),
                ('population', models.PositiveIntegerField()),
                ('telephone_number', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('zip_code', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999)])),
                ('credit_card', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999999999)])),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('product_code', models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('product_name', models.CharField(max_length=150)),
                ('description_product', models.CharField(max_length=300)),
                ('supplier_code', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('unity_price', models.PositiveIntegerField()),
                ('unit_in_stock', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('order_code', models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('order_number', models.PositiveIntegerField()),
                ('client_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='simple_db.client')),
                ('product_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='simple_db.products')),
            ],
        ),
    ]