# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_auto_20150105_0015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='house',
            name='status',
            field=models.CharField(default=b'unsecured', max_length=9, choices=[(b'secure', b'Secure'), (b'unsecured', b'Unsecured')]),
        ),
    ]
