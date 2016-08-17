# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models, migrations


def null_dates(apps, schema_editor):
    House = apps.get_model("board", "House")
    House.objects.filter(updated_at__isnull=True).update(updated_at=datetime(year=1970, month=1, day=1))

class Migration(migrations.Migration):

    dependencies = [
        ('board', '0012_auto_20160814_1517'),
    ]

    operations = [
        migrations.RunPython(null_dates),
    ]
