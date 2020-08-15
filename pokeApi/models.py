from django.db import models

class Pokemon(models.Model):
    id_poke = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    base_stats = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()

class Evolution(models.Model):
    id_evo = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    type = models.CharField(max_length=30)
    level = models.IntegerField(default=0)
