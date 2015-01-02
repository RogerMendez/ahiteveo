# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_auto_20141224_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='portada',
            field=models.ImageField(upload_to=b'productos', null=True, verbose_name=b'Portada de Producto', blank=True),
            preserve_default=True,
        ),
    ]
