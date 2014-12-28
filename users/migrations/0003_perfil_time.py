# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20140925_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='time',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
