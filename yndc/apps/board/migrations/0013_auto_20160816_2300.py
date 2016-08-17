# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models, migrations


def null_dates(apps, schema_editor):
    House = apps.get_model("board", "House")
    for house in House.objects.filter(updated_at__isnull=True):
        House.objects.filter(pk=house.pk).update(updated_at=house.created_at)

class Migration(migrations.Migration):

    dependencies = [
        ('board', '0012_auto_20160814_1517'),
    ]

    operations = [
        migrations.RunPython(null_dates),
    ]
