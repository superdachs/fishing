from django.db import models
from django_countries.fields import CountryField

class Fish(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Water(models.Model):
    name = models.CharField(max_length=255)
    country = CountryField(null=True)
    federal_state = models.ForeignKey('FederalState', null=True, blank=True)
    max_depth = models.IntegerField()
    water_id = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    fishes = models.ManyToManyField('Fish')

    def __str__(self):
        return self.name

class FederalState(models.Model):
    name = models.CharField(max_length=255)
    country = CountryField()

    def __str__(self):
        return self.name
