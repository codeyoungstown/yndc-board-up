# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20141214_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='status',
            field=models.CharField(default=b'secure', max_length=8, choices=[(b'secure', b'Secure'), (b'unsecured', b'Unsecured')]),
        ),
    ]
