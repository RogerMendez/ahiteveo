# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_imagenes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorias',
            name='nombre',
            field=models.CharField(unique=True, max_length=b'20'),
        ),
    ]
