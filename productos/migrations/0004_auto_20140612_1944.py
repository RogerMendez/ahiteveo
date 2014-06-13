# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20140612_0006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=b'100')),
                ('registro', models.DateTimeField(auto_now_add=True)),
                ('estado', models.BooleanField(default=False)),
                ('categoria', models.ForeignKey(to='productos.Categorias', to_field='id', null=True)),
            ],
            options={
                'ordering': [b'nombre'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='categorias',
            name='estado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='categorias',
            name='registro',
            field=models.DateTimeField(default=datetime.date(2014, 6, 12), auto_now_add=True),
            preserve_default=False,
        ),
    ]
