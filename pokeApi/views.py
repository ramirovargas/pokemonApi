import json

from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from pokeApi.models import Pokemon, Evolution
from pokeApi.serializers import PokemonSerializer, EvolutionSerializer


@api_view(['GET'])
def pokemon_element(request, name):
    try:
        pokemon = Pokemon.objects.get(name=name)
    except Pokemon.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        result=[]
        evolutions=get_evolutions(pokemon)
        for i in evolutions:
            result.append(EvolutionSerializer(i).data)
        serializer_poke = PokemonSerializer(pokemon)
        data_set = {"pokemon_data": serializer_poke.data,"evolution_data":result}
        json_result = data_set

        return Response(json_result)

def get_evolutions(poke):
    return Evolution.objects.filter(pokemon=poke)