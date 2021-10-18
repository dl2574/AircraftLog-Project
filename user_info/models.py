from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, DO_NOTHING


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE, null=True, blank=True)
    rank = models.ForeignKey('Rank', on_delete=DO_NOTHING, null=True, blank=True)
    fname = models.CharField(max_length=100, blank=True)
    lname = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=50, blank=True, unique=True)
    crew_position = models.ForeignKey('CrewPosition', on_delete=DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.lname + ", " + self.fname

class Rank(models.Model):
    rank = models.CharField(max_length=10)

    def __str__(self):
        return self.rank

class CrewPosition(models.Model):
    crew_position = models.CharField(max_length=50)

    def __str__(self):
        return self.crew_position


