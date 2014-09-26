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
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=b'100')),
            ],
            options={
                'verbose_name_plural': 'Ciudades',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=b'100')),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Paices',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(upload_to=b'avatar')),
                ('telefono', models.CharField(max_length=b'10')),
                ('direccion', models.CharField(max_length=b'100')),
                ('fecha_nacimiento', models.DateField(default=None, verbose_name=b'Fecha de Nacimiento')),
                ('code_activation', models.CharField(max_length=b'100', null=True, blank=True)),
                ('tipo', models.CharField(blank=True, max_length=b'10', null=True, choices=[(b'Empresa', b'Empresa'), (b'Personal', b'Personal')])),
                ('ciudad', models.ForeignKey(blank=True, to='users.Ciudad', null=True)),
                ('usuario', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='pais',
            field=models.ForeignKey(to='users.Pais'),
            preserve_default=True,
        ),
    ]
