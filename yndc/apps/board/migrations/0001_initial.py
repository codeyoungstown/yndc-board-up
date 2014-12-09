# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('type', models.CharField(default=b'vacant-cleanup', max_length=255, choices=[(b'vacant-cleanup', b'Vacant cleanup'), (b'occupied-repair', b'Occupied repair'), (b'vacant-rehab', b'Vacant rehab'), (b'vacant-lot', b'Vacant lot reuse')])),
                ('archived', models.BooleanField(default=False)),
                ('tires_picked_up', models.PositiveIntegerField(help_text=b'Tires picked up.')),
                ('bags_of_trash', models.PositiveIntegerField(help_text=b'Bags of trash removed.')),
                ('cubic_yards_of_debris', models.PositiveIntegerField(help_text=b'Cubic yards of debris removed.')),
                ('linear_feet_sidewalk_scraped', models.PositiveIntegerField(help_text=b'Linear feer of sidewalk scraped.')),
                ('boards_cut', models.PositiveIntegerField(help_text=b'Boards cut.')),
                ('vacant_structures_cleaned', models.PositiveIntegerField(help_text=b'Vacant structures boarded / cleaned up.')),
                ('vacant_lots_repurposed', models.PositiveIntegerField(help_text=b'Vacant lots repurposed.')),
                ('occupied_homes_repaired', models.PositiveIntegerField(help_text=b'Occupied homes repaired.')),
                ('vacant_homes_rehabed', models.PositiveIntegerField(help_text=b'Vacant homes repaired.')),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('photo', easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'yndc-photos')),
                ('status', models.CharField(default=b'secure', max_length=8, choices=[(b'secure', b'Secure'), (b'insecure', b'Insecure')])),
                ('requested_by', models.CharField(default=b'Y', max_length=8, choices=[(b'Y', b'YNDC'), (b'C', b'City'), (b'N', b'Neighborhood')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('archived', models.BooleanField(default=False)),
                ('outside_check_lawn_work', models.BooleanField(default=False, help_text=b'Significant lawn work.')),
                ('outside_check_reclaim_sidewalk', models.BooleanField(default=False, help_text=b'Reclaim sidewalk.')),
                ('outside_check_reclaim_driveway', models.BooleanField(default=False, help_text=b'Reclaim driveway.')),
                ('outside_check_shrubs_trim', models.BooleanField(default=False, help_text=b'Shrubs - trim back.')),
                ('outside_check_shrubs_cut', models.BooleanField(default=False, help_text=b'Shrubs - cut down.')),
                ('outside_check_large_amt_brush', models.BooleanField(default=False, help_text=b'Large amount of brush.')),
                ('removal_check_remove_debris', models.BooleanField(default=False, help_text=b'Remove debris.')),
                ('removal_check_remove_trash', models.BooleanField(default=False, help_text=b'Remove trash.')),
                ('removal_check_remove_weeds', models.BooleanField(default=False, help_text=b'Remove weeds.')),
                ('removal_check_remove_leaves', models.BooleanField(default=False, help_text=b'Rake and remove leaves.')),
                ('removal_check_remove_tires', models.BooleanField(default=False, help_text=b'Remove tires.')),
                ('removal_check_prophylactics', models.BooleanField(default=False, help_text=b'Remove prophylactics.')),
                ('removal_check_other', models.BooleanField(default=False, help_text=b'OTHER.')),
                ('general_check_bees', models.BooleanField(default=False, help_text=b'Bee or wasp hazard on site. Bring spray.')),
                ('general_check_chainsaw', models.BooleanField(default=False, help_text=b'Bring chainsaw to cut thick brush.')),
                ('general_check_dumpster', models.BooleanField(default=False, help_text=b'Site needs a dumpster.')),
                ('general_check_large_project', models.BooleanField(default=False, help_text=b'Site is a large project and will take more than typical time to complete.')),
                ('general_check_collapsed_porch', models.BooleanField(default=False, help_text=b'Collapsed porch/steps.')),
                ('general_check_falling_debris', models.BooleanField(default=False, help_text=b'Risk of falling debris.')),
                ('general_check_poison_ivy', models.BooleanField(default=False, help_text=b'Poison ivy.')),
                ('general_check_blocked_openings', models.BooleanField(default=False, help_text=b'Blocked openings.')),
                ('general_check_broken_glass', models.BooleanField(default=False, help_text=b'Broken glass.')),
                ('general_check_wildlife_hazard', models.BooleanField(default=False, help_text=b'Wildlife hazard.')),
                ('general_check_metal_window_frames', models.BooleanField(default=False, help_text=b'Metal window frames. May be difficult to nail on.')),
                ('general_check_brick_stone', models.BooleanField(default=False, help_text=b'Brick/stone house. Measurements must be tight.')),
                ('general_check_clear_brush', models.BooleanField(default=False, help_text=b'Clear cut brush in front and around property.')),
                ('general_check_tires', models.BooleanField(default=False, help_text=b'Put all tires at the site on the curb.')),
                ('general_check_clean_trash', models.BooleanField(default=False, help_text=b'Clean up trash and debris from the yard.')),
                ('general_check_preserve_landscaping', models.BooleanField(default=False, help_text=b'Preserve any landscaping shrubs on site and trim them.')),
                ('general_check_limb', models.BooleanField(default=False, help_text=b'Limb up overgrown trees.')),
                ('general_check_mow', models.BooleanField(default=False, help_text=b'Mow, clear cut, and rake lawn.')),
                ('general_check_flower_beds', models.BooleanField(default=False, help_text=b'Clea out flower beds.')),
                ('general_check_paint', models.BooleanField(default=False, help_text=b'Paint existing boards.')),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='house',
            name='neighborhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='board.Neighborhood', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='house',
            field=models.ForeignKey(related_name=b'events', to='board.House'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='board',
            name='house',
            field=models.ForeignKey(related_name=b'boards', to='board.House'),
            preserve_default=True,
        ),
    ]
