from django.core.management.base import BaseCommand

from pokeApi.services import get_from_url


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Indicates id of evolution chain')

    def handle(self, *args, **kwargs):
        main_url = "https://pokeapi.co/api/v2/evolution-chain/"
        id = kwargs['id']
        response=get_from_url(main_url+str(id))
        for evol_key, evol_value in response.json().items():
            if(evol_key=="chain"):
                for chain_key, chain_value in evol_value.items():
                    if(chain_key=="species"):
                        self.get_pokemon_char(list(chain_value.items())[0][1])

    def get_pokemon_char(self, name):
        pokemon_url = "https://pokeapi.co/api/v2/pokemon/"
        response = get_from_url(pokemon_url + name)
        for poke_key, poke_value in response.json().items():
            print(poke_key)



    def save_pokemon(self,pokemon):
        pokemon.save()

    def save_evolution(self,evolution):
        evolution.save()
