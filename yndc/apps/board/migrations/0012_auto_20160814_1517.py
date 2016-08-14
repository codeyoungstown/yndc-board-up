# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0011_house_updated_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='house',
            options={'ordering': ['-updated_at']},
        ),
    ]
