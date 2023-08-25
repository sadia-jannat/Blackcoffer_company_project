from django.db import models

# Create your models here.

class Energy(models.Model):
    end_year = models.CharField(max_length=100)
    intensity = models.IntegerField()
    sector = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    insight = models.CharField(max_length=100)
    url = models.URLField()
    region = models.CharField(max_length=100)
    start_year = models.CharField(max_length=100)
    impact = models.CharField(max_length=100)
    added = models.TextField(max_length=100)
    published = models.TextField(max_length=100)
    country = models.CharField(max_length=100)
    relevance = models.IntegerField()
    pestle = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    likelihood = models.IntegerField()

    def __str__(self):
        return self.title


class EnergyProject(models.Model):
    end_year = models.CharField(max_length=100)
    intensity = models.IntegerField()
    sector = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    insight = models.CharField(max_length=100)
    url = models.URLField()
    region = models.CharField(max_length=100)
    start_year = models.CharField(max_length=100)
    impact = models.CharField(max_length=100)
    added = models.TextField(max_length=100)
    published = models.TextField(max_length=100)
    country = models.CharField(max_length=100)
    relevance = models.IntegerField()
    pestle = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    likelihood = models.IntegerField()

    def __str__(self):
        return self.sector