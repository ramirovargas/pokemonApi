from django.db import models

class Pokemon(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    base_stats = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    evolutions = models.TextField(null=True)