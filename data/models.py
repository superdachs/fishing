from django.db import models
from django_countries.fields import CountryField
from djangoyearlessdate.models import YearlessDateField

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

class ProtectionTime(models.Model):
    fish = models.ForeignKey('Fish')
    country = CountryField(null=True, blank=True)
    federal_state = models.ForeignKey('FederalState', null=True, blank=True)
    water = models.ForeignKey('Water', null=True, blank=True)
    start = YearlessDateField()
    end = YearlessDateField()

    def __str__(self):
        return self.country.name + self.federal_state.name + self.water.name

class ProtectionLength(models.Model):
    fish = models.ForeignKey('Fish')
    country = CountryField(null=True, blank=True)
    federal_state = models.ForeignKey('FederalState', null=True, blank=True)
    water = models.ForeignKey('Water', null=True, blank=True)
    length = models.IntegerField()

    def __str__(self):
        return self.country.name + self.federal_state.name + self.water.name

