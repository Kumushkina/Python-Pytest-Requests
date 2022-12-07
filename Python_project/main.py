import requests
import json

token = '706e23b8e07b2918b8bb209b26386589'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "name": "пес",
    "photo": "https://e7.pngegg.com/pngimages/265/977/png-clipart-pokemon-platinum-umbreon-pikachu-pokemon-vrste-others-mammal-cat-like-mammal.png"
})

print(response.text)


response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": 1455,
    "name": "пес, будешь майонез",
    "photo": "https://e7.pngegg.com/pngimages/265/977/png-clipart-pokemon-platinum-umbreon-pikachu-pokemon-vrste-others-mammal-cat-like-mammal.png"
})

print(response_put.text)


response_post = requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers={'trainer_token' : token}, json={
    "pokemon_id": 1455
})

print(response_post.text)