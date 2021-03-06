# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-14 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedore',
            name='apellido_contacto',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedore',
            name='correo_contacto',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='proveedore',
            name='correo_empresa',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='proveedore',
            name='nombre_contacto',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedore',
            name='telefono_contacto',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
