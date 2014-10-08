# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20141004_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(upload_to=b'productos', verbose_name=b'Seleccionar Imagen')),
                ('producto', models.ForeignKey(blank=True, to='productos.Productos', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
