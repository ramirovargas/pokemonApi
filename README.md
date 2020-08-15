# pokemonApi

Ejemplo de peticion

Pokemon Element
GET /pokemon/charmander
HTTP 200 OK
Allow: OPTIONS, GET
Content-Type: application/json
Vary: Accept


Ejemplo respuesta 
```
{
    "pokemon_data": {
        "id_poke": 4,
        "name": "charmander",
        "weight": 85,
        "height": 6,
        "base_stats": 39
    },
    "evolution_data": [
        {
            "id_evo": 5,
            "name": "charmeleon",
            "type": "Evolution",
            "poke": "charmander"
        },
        {
            "id_evo": 6,
            "name": "charizard",
            "type": "Evolution",
            "poke": "charmander"
        }
    ]
}
```
Decisiones para obtener datos de los pokemon:

*   Se guardan cada uno de los pokemons de sus evoluciones
*   Se añade campo level para saber el nivel del pokemon en la relacion con su evolucion
*   Se calcula con el dato del pokemon que otro hay con ese Id y se calcula si es evolucion o Preevolucion

Nota: Se añade directorio venv o puedes usar tu propio ambiente virtual instalando las librerias de requirement.txt
