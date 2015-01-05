# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_house_additional_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='requested_by',
            field=models.CharField(default=b'Y', max_length=8, choices=[(b'Y', b'YNDC'), (b'C', b'City'), (b'N', b'Neighborhood'), (b'L', b'Lank Bank')]),
        ),
    ]
