from django.core.management.base import BaseCommand

from pokeApi.models import Pokemon, Evolution
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
                        pokemon=self.get_pokemon_char(list(chain_value.items())[0][1])
                    if(chain_key=="evolves_to"):
                        evolves=chain_value
        self.get_evolution_poke(pokemon, evolves)

    def get_pokemon_char(self, name):
        pokemon_url = "https://pokeapi.co/api/v2/pokemon/"
        response = get_from_url(pokemon_url + name)
        for poke_key, poke_value in response.json().items():
            if(poke_key=="id"):
                id=poke_value
            if (poke_key == "weight"):
                weight=poke_value
            if (poke_key == "height"):
                height=poke_value
            if (poke_key == "stats"):
                base_stats=list(poke_value[0].items())[0][1]
        pokemon= Pokemon(id_poke=id,name=name,weight=weight,height=height,base_stats=base_stats)
        self.save_pokemon(pokemon)
        return pokemon

    def get_evolution_poke(self,pokemon,evolution):
        # Segun entendi de la api solo me da la evolucion hacia arriba
        for evol_key, evol_value in evolution[0].items():
            if(evol_key=="is_baby"):
                if(evol_value):
                    type="Preevolution"
                else:
                    type="Evolution"
            if(evol_key=="species"):
                name=list(evol_value.items())[0][1]
                evolution=Evolution(id_evo = self.get_id_poke(name), name = name , pokemon = pokemon , type = type)
                self.save_evolution(evolution)

    def get_id_poke(self,name):
        pokemon_url = "https://pokeapi.co/api/v2/pokemon/"
        response = get_from_url(pokemon_url + name)
        for poke_key, poke_value in response.json().items():
            if(poke_key=="id"):
                id=poke_value
        return id


    def save_pokemon(self,pokemon):
        pokemon.save()

    def save_evolution(self,evolution):
        evolution.save()
