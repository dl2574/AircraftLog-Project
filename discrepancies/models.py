from django.db import models
from django.db.models.fields.related import ForeignKey
from Aircraft.models import Aircraft

class Discrepancy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_discovered = models.DateField(null=True, blank=True)
    date_resolved = models.DateField(null=True, blank=True)
    aircraft_id = ForeignKey(Aircraft, on_delete=models.CASCADE)
    #discovered_by

    def __str__(self):
        return self.title


