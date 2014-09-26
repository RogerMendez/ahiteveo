# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='fecha_nacimiento',
            field=models.DateField(null=True, verbose_name=b'Fecha de Nacimiento'),
        ),
    ]
