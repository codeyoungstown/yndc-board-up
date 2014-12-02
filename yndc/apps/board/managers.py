from django.db import models


class HouseManager(models.Manager):
    def active(self):
        return self.select_related('neighborhood').exclude(archived=True)


class EventManager(models.Manager):
    def active(self):
        return self.exclude(archived=True)
