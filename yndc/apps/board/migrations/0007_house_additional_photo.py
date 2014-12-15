# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_auto_20141215_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='additional_photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(default='', upload_to=b'yndc-photos', blank=True),
            preserve_default=False,
        ),
    ]
