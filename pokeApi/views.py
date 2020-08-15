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
        if(len(result)==0):
            evolution_from=get_evolutions_from_name(pokemon.name)
            poke_origin=evolution_from.first().pokemon
            if(evolution_from.first().level==1):
                id_evo=evolution_from.first().id_evo-1
            else:
                id_evo = evolution_from.first().id_evo-2
            evolution=Evolution(id_evo = id_evo, name = poke_origin.name , pokemon = poke_origin , type = "Preevolution" ,level=0)
            result.append(EvolutionSerializer(evolution).data)
            third_evolution=get_evolutions(poke_origin)
            if (evolution_from.first().level == 1):
                for j in third_evolution:
                    if(j.level==2):
                        result.append(EvolutionSerializer(j).data)
            else:
                for j in third_evolution:
                    if(j.level==1):
                        setattr(j, "type", "Preevolution")
                        result.append(EvolutionSerializer(j).data)

        serializer_poke = PokemonSerializer(pokemon)
        data_set = {"pokemon_data": serializer_poke.data,"evolution_data":result}
        json_result = data_set

        return Response(json_result)

def get_evolutions(poke):
    return Evolution.objects.filter(pokemon=poke)

def get_evolutions_from_name(name):
    return Evolution.objects.filter(name=name)
