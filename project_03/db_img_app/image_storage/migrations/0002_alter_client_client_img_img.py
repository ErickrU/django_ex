# Generated by Django 3.2.5 on 2021-07-09 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_storage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_img_img',
            field=models.ImageField(blank=True, upload_to='clients_images/'),
        ),
    ]
