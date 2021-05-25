# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bytesports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='location_field',
            field=models.CharField(default='Zamora colonia 4 calle 5', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='match_hour',
            field=models.CharField(default='5:50', max_length=6),
            preserve_default=False,
        ),
    ]
