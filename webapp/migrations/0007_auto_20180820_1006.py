# Generated by Django 2.0.8 on 2018-08-20 15:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20180820_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='fecha_de_actualizacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='fecha_de_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
