from django.db import models

class Aircraft(models.Model):
    serial_number = models.CharField(max_length=10, primary_key=True, unique=True)
    tail_number = models.CharField(max_length=10, blank=True)
    mods = models.ManyToManyField('Mod', blank=True)


    def __str__(self):
        return self.serial_number

class Mod(models.Model):
    tcto = models.CharField(max_length=50, primary_key=True, unique=True)
    short_name = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.short_name

