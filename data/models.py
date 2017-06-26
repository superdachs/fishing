from django.db import models
from django_countries.fields import CountryField

class Fish(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Water(models.Model):
    name = models.CharField(max_length=255)
    country = CountryField()
    federal_state = models.ForeignKey('FederalState', null=True, blank=True)
    max_depth = models.IntegerField()



    def __str__(self):
        return self.name

class FederalState(models.Model):
    name = models.CharField(max_length=255)
    country = CountryField()

    def __str__(self):
        return self.name
