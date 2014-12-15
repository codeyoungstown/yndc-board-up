# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def unsecured(apps, schema_editor):
    House = apps.get_model("board", "House")
    House.objects.filter(status='insecure').update(status='unsecured')


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20141215_0022'),
    ]

    operations = [
        migrations.RunPython(unsecured),
    ]
