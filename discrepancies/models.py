from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields.related import ForeignKey
from Aircraft.models import Aircraft
from user_info.models import Profile

class Discrepancy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_discovered = models.DateField(null=True, blank=True)
    date_resolved = models.DateField(null=True, blank=True)
    aircraft_id = ForeignKey(Aircraft, on_delete=models.CASCADE)
    discovered_by = ForeignKey(Profile, on_delete=DO_NOTHING, null=True)
    occurrences = models.IntegerField(default=0)

    class Meta:
        ordering = ['-date_resolved', '-occurrences', '-date_discovered']

    def __str__(self):
        return self.title


