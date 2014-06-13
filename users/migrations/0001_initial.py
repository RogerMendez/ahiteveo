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
                'verbose_name_plural': b'Ciudades',
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
                'ordering': [b'nombre'],
                'verbose_name_plural': b'Paices',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='pais',
            field=models.ForeignKey(to='users.Pais', to_field='id'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(upload_to=b'avatar')),
                ('telefono', models.CharField(max_length=b'10')),
                ('direccion', models.CharField(max_length=b'100')),
                ('ciudad', models.ForeignKey(to_field='id', blank=True, to='users.Ciudad', null=True)),
                ('user', models.OneToOneField(null=True, to_field='id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
