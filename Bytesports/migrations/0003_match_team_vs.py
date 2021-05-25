# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bytesports', '0002_auto_20150821_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='team_vs',
            field=models.CharField(default='Equipo Prueba', max_length=50),
            preserve_default=False,
        ),
    ]
