from django.db import models
from django.utils.text import slugify


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
    address = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    neighborhood = models.ForeignKey(Neighborhood, blank=True, null=True)
    notes = models.TextField(blank=True)

    photo = models.ImageField(upload_to='yndc-photos')

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
        help_text='Clea out flower beds.')
    general_check_paint = models.BooleanField(default=False,
        help_text='Paint existing boards.')

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
    width = models.IntegerField()
    height = models.IntegerField()
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s - %s H x %s W' % (self.description, self.height, self.width)
