# pokemonApi

Ejemplo de peticion

Pokemon Element
GET /pokemon/squirtle
HTTP 200 OK
Allow: OPTIONS, GET
Content-Type: application/json
Vary: Accept


Ejemplo respuesta 
```
{
    "pokemon_data": {
        "id_poke": 7,
        "name": "squirtle",
        "weight": 90,
        "height": 5,
        "base_stats": 44
    },
    "evolution_data": [
        {
            "id_evo": 8,
            "name": "wartortle",
            "type": "Evolution",
            "poke": "squirtle"
        }
    ]
}
```

Nota: Se añade directorio venv o puedes usar tu propio ambiente virtual instalando las librerias de requirement.txt
