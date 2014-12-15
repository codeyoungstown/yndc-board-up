from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

from easy_thumbnails.fields import ThumbnailerImageField

from board.managers import EventManager, HouseManager


class Neighborhood(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(blank=True)

    def __unicode__(self):
        return self.name

    def save(self):
        if not self.slug:
            slug = slugify(self.name)
            slug_to_save = slug
            
            count = 1
            while self.__class__.objects.filter(slug=slug_to_save).exists():
                slug_to_save = '%s-%s' % (slug, count)
                count += 1
            self.slug = slug_to_save
        super(Neighborhood, self).save()


class House(models.Model):
    STATUS_SECURE = 'secure'
    STATUS_INSECURE = 'insecure'

    STATUS_CHOICES = (
        (STATUS_SECURE, 'Secure'),
        (STATUS_INSECURE, 'Insecure'),
    )

    REQUESTED_BY_YNDC = 'Y'
    REQUESTED_BY_CITY = 'C'
    REQUESTED_BY_NEIGHBORHOOD = 'N'

    REQUESTED_BY = (
        (REQUESTED_BY_YNDC, 'YNDC'),
        (REQUESTED_BY_CITY, 'City'),
        (REQUESTED_BY_NEIGHBORHOOD, 'Neighborhood'),
    )

    address = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, db_index=True)
    neighborhood = models.ForeignKey(Neighborhood, blank=True, null=True,
        on_delete=models.SET_NULL)
    notes = models.TextField(blank=True)
    photo = ThumbnailerImageField(upload_to='yndc-photos')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES,
        default=STATUS_SECURE)
    requested_by = models.CharField(max_length=8, choices=REQUESTED_BY,
        default=REQUESTED_BY_YNDC)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)

    archived = models.BooleanField(default=False)

    # Outside checklist
    outside_check_lawn_work = models.BooleanField(default=False,
        help_text='Significant lawn work.')
    outside_check_reclaim_sidewalk = models.BooleanField(default=False,
        help_text='Reclaim sidewalk.')
    outside_check_reclaim_driveway = models.BooleanField(default=False,
        help_text='Reclaim driveway.')
    outside_check_shrubs_trim = models.BooleanField(default=False,
        help_text='Shrubs - trim back.')
    outside_check_shrubs_cut = models.BooleanField(default=False,
        help_text='Shrubs - cut down.')
    outside_check_large_amt_brush = models.BooleanField(default=False,
        help_text='Large amount of brush.')

    # Removal checklist
    removal_check_remove_debris = models.BooleanField(default=False,
        help_text='Remove debris.')
    removal_check_remove_trash = models.BooleanField(default=False,
        help_text='Remove trash.')
    removal_check_remove_weeds = models.BooleanField(default=False,
        help_text='Remove weeds.')
    removal_check_remove_leaves = models.BooleanField(default=False,
        help_text='Rake and remove leaves.')
    removal_check_remove_tires = models.BooleanField(default=False,
        help_text='Remove tires.')
    removal_check_prophylactics = models.BooleanField(default=False,
        help_text='Remove prophylactics.')
    removal_check_other = models.BooleanField(default=False,
        help_text='OTHER.')

    # General checklist
    general_check_bees = models.BooleanField(default=False,
        help_text='Bee or wasp hazard on site. Bring spray.')
    general_check_chainsaw = models.BooleanField(default=False,
        help_text='Bring chainsaw to cut thick brush.')
    general_check_dumpster = models.BooleanField(default=False,
        help_text='Site needs a dumpster.')
    general_check_large_project = models.BooleanField(default=False,
        help_text='Site is a large project and will take more than typical '
        'time to complete.')
    general_check_collapsed_porch = models.BooleanField(default=False,
        help_text='Collapsed porch/steps.')
    general_check_falling_debris = models.BooleanField(default=False,
        help_text='Risk of falling debris.')
    general_check_poison_ivy = models.BooleanField(default=False,
        help_text='Poison ivy.')
    general_check_blocked_openings = models.BooleanField(default=False,
        help_text='Blocked openings.')
    general_check_broken_glass = models.BooleanField(default=False,
        help_text='Broken glass.')
    general_check_wildlife_hazard = models.BooleanField(default=False,
        help_text='Wildlife hazard.')
    general_check_metal_window_frames = models.BooleanField(default=False,
        help_text='Metal window frames. May be difficult to nail on.')
    general_check_brick_stone = models.BooleanField(default=False,
        help_text='Brick/stone house. Measurements must be tight.')
    general_check_clear_brush = models.BooleanField(default=False,
        help_text='Clear cut brush in front and around property.')
    general_check_tires = models.BooleanField(default=False,
        help_text='Put all tires at the site on the curb.')
    general_check_clean_trash = models.BooleanField(default=False,
        help_text='Clean up trash and debris from the yard.')
    general_check_preserve_landscaping = models.BooleanField(default=False,
        help_text='Preserve any landscaping shrubs on site and trim them.')
    general_check_limb = models.BooleanField(default=False,
        help_text='Limb up overgrown trees.')
    general_check_mow = models.BooleanField(default=False,
        help_text='Mow, clear cut, and rake lawn.')
    general_check_flower_beds = models.BooleanField(default=False,
        help_text='Clear out flower beds.')
    general_check_paint = models.BooleanField(default=False,
        help_text='Paint existing boards.')

    objects = HouseManager()

    def __unicode__(self):
        return self.address

    def save(self):
        if not self.slug:
            slug = slugify(self.address)
            slug_to_save = slug

            count = 1
            while self.__class__.objects.filter(slug=slug_to_save).exists():
                slug_to_save = '%s-%s' % (slug, count)
                count += 1
            self.slug = slug_to_save
        super(House, self).save()

    def _get_checklist(self, prefix):
        checks = []
        for x in self._meta.fields:
            if x.name.startswith(prefix) and getattr(self, x.name):
                check = {
                    'title': x.help_text,
                    'value': getattr(self, x.name, False)
                }
                checks.append(check)
        return checks

    def outside_checklist(self):
        return self._get_checklist('outside_check')

    def removal_checklist(self):
        return self._get_checklist('removal_check')

    def general_checklist(self):
        return self._get_checklist('general_check')


class Board(models.Model):
    house = models.ForeignKey(House, related_name='boards')
    width = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s - %s H x %s W' % (self.description, self.height, self.width)


class Event(models.Model):
    EVENT_TYPE_VACANT_CLEANUP = 'vacant-cleanup'
    EVENT_TYPE_OCCUPIED_REPAIR = 'occupied-repair'
    EVENT_TYPE_VACANT_REHAB = 'vacant-rehab'
    EVENT_TYPE_VACANT_LOT = 'vacant-lot'

    EVENT_TYPES = (
        (EVENT_TYPE_VACANT_CLEANUP, 'Vacant cleanup'),
        (EVENT_TYPE_OCCUPIED_REPAIR, 'Occupied repair'),
        (EVENT_TYPE_VACANT_REHAB, 'Vacant rehab'),
        (EVENT_TYPE_VACANT_LOT, 'Vacant lot reuse')
    )

    house = models.ForeignKey(House, related_name='events')
    date = models.DateTimeField()
    type = models.CharField(max_length=255, choices=EVENT_TYPES,
        default=EVENT_TYPE_VACANT_CLEANUP)

    created_by = models.ForeignKey(User)

    archived = models.BooleanField(default=False)

    # Counts
    tires_picked_up = models.PositiveIntegerField(help_text='Tires picked up.')
    bags_of_trash = models.PositiveIntegerField(help_text='Bags of trash removed.')
    cubic_yards_of_debris = models.PositiveIntegerField(help_text='Cubic yards of debris removed.')
    linear_feet_sidewalk_scraped = models.PositiveIntegerField(help_text='Linear feer of sidewalk scraped.')
    boards_cut = models.PositiveIntegerField(help_text='Boards cut.')
    vacant_structures_cleaned = models.PositiveIntegerField(help_text='Vacant structures boarded / cleaned up.')
    vacant_lots_repurposed = models.PositiveIntegerField(help_text='Vacant lots repurposed.')
    occupied_homes_repaired = models.PositiveIntegerField(help_text='Occupied homes repaired.')
    vacant_homes_rehabed = models.PositiveIntegerField(help_text='Vacant homes repaired.')

    objects = EventManager()
