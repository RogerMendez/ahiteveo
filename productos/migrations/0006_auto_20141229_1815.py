# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_productos_portada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenes',
            name='imagen',
            field=models.ImageField(upload_to=b'productos', verbose_name=b'Agregar Imagenes'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='portada',
            field=models.ImageField(upload_to=b'productos', verbose_name=b'Portada de Producto', blank=True),
        ),
    ]
