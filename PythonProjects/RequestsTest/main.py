"""
Kolorado tests api
"""

import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': 'd671a1ecb0b56549fa4469d2c1a1a7c0'
}

body = {
    "name": "generate",
    "photo": "generate"
}

BODY = {
    "pokemon_id": "28204",
    "name": "Мармышка",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}



response = requests.post(url= f'{URL}/pokemons', json=body, headers=HEADER, timeout=20)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')

response = requests.put(url= f'{URL}/pokemons', json=BODY, headers=HEADER, timeout=20)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')

response = requests.post(url= f'{URL}/trainers/add_pokeball', json={
    "pokemon_id": "28294"
}, headers=HEADER, timeout=20)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')