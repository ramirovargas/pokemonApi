from rest_framework import serializers

from pokeApi import models
from pokeApi.models import Pokemon, Evolution


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('id_poke', 'name', 'weight', 'height', 'base_stats')


class EvolutionSerializer(serializers.ModelSerializer):
    poke = serializers.CharField(source='pokemon.name', read_only=True)
    class Meta:
        model = Evolution
        fields = ('id_evo', 'name', 'type' ,'poke')