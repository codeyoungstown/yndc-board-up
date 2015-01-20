# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_auto_20150105_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='bags_of_trash',
            field=models.PositiveIntegerField(default=0, help_text=b'Bags of trash removed.'),
        ),
        migrations.AlterField(
            model_name='event',
            name='boards_cut',
            field=models.PositiveIntegerField(default=0, help_text=b'Boards cut.'),
        ),
        migrations.AlterField(
            model_name='event',
            name='cubic_yards_of_debris',
            field=models.PositiveIntegerField(default=0, help_text=b'Cubic yards of debris removed.'),
        ),
        migrations.AlterField(
            model_name='event',
            name='linear_feet_sidewalk_scraped',
            field=models.PositiveIntegerField(default=0, help_text=b'Linear feer of sidewalk scraped.'),
        ),
        migrations.AlterField(
            model_name='event',
            name='occupied_homes_repaired',
            field=models.PositiveIntegerField(default=0, help_text=b'Occupied homes repaired.'),
        ),
        migrations.AlterField(
            model_name='event',
            name='tires_picked_up',
            field=models.PositiveIntegerField(default=0, help_text=b'Tires picked up.'),
        ),
        migrations.AlterField(
            model_name='event',
            name='vacant_homes_rehabed',
            field=models.PositiveIntegerField(default=0, help_text=b'Vacant homes repaired.'),
        ),
        migrations.AlterField(
            model_name='event',
            name='vacant_lots_repurposed',
            field=models.PositiveIntegerField(default=0, help_text=b'Vacant lots repurposed.'),
        ),
        migrations.AlterField(
            model_name='event',
            name='vacant_structures_cleaned',
            field=models.PositiveIntegerField(default=0, help_text=b'Vacant structures boarded / cleaned up.'),
        ),
    ]
