# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productos', '0004_auto_20140612_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=b'100')),
                ('descripcion', models.TextField()),
                ('registro', models.DateTimeField(auto_now_add=True)),
                ('tipo', models.ManyToManyField(to='productos.Tipo')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id', unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
