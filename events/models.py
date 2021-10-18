from django.db import models
from Aircraft.models import Aircraft

class Event(models.Model):
    short_name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    event_date = models.DateField(blank=True, null=True)
    event_time = models.TimeField(blank=True, null=True)
    event_date_end = models.DateField(blank=True, null=True)
    aircraft = models.ManyToManyField(Aircraft, blank=True)
    lives_saved = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.short_name
