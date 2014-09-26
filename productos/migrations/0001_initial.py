# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=b'100')),
                ('registro', models.DateTimeField(auto_now_add=True)),
                ('estado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Categorias',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=b'100')),
                ('descripcion', models.TextField()),
                ('registro', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=b'100')),
                ('registro', models.DateTimeField(auto_now_add=True)),
                ('estado', models.BooleanField(default=False)),
                ('categoria', models.ForeignKey(to='productos.Categorias', null=True)),
            ],
            options={
                'ordering': ['categoria'],
                'verbose_name_plural': 'Tipos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='productos',
            name='tipo',
            field=models.ManyToManyField(to='productos.Tipo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='productos',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=True,
        ),
    ]
