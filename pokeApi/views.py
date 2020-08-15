from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from pokeApi.models import Pokemon
from pokeApi.serializers import PokemonSerializer


@api_view(['GET'])
def pokemon_element(request, name):
    try:
        pokemon = Pokemon.objects.get(name=name)
    except Pokemon.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data)