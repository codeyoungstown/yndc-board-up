from django.db import models


class HouseManager(models.Manager):
    def active(self):
        return self.exclude(archived=True)
