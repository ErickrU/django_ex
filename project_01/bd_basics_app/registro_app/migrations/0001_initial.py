# Generated by Django 3.2.4 on 2021-06-12 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('no_control', models.CharField(max_length=10)),
                ('cuatrimestres', models.CharField(max_length=5)),
                ('grupo', models.CharField(max_length=10)),
            ],
        ),
    ]
