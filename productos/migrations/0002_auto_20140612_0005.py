# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorias',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id', null=True),
        ),
    ]
