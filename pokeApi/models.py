from django.db import models

class Pokemon(models.Model):
    Id = models.IntegerField()
    name = models.CharField(max_length=30)
    base_stats = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()

class Evolution(models.Model):
    Id = models.IntegerField()
    name = models.CharField(max_length=30)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    type = models.CharField(max_length=30)
