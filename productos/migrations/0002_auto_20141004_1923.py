# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipo',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Tipos'},
        ),
        migrations.AlterField(
            model_name='categorias',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='usuario',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
