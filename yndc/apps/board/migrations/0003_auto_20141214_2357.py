# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20141208_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='general_check_flower_beds',
            field=models.BooleanField(default=False, help_text=b'Clear out flower beds.'),
        ),
    ]
