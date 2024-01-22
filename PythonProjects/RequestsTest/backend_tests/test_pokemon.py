import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': 'd671a1ecb0b56549fa4469d2c1a1a7c0'
}

def test_get_trainers():
    """
    KTI-1. Get trainers by code 200
    """
    response = requests.get(url= f'{URL}/trainers', params={'level': 1}, headers=HEADER, timeout=20)
    assert response.status_code == 200, 'Unexpected status code'
    
def test_get_trainers_by_id():
    """
    KTI-2. Get trainers by id
    """
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': 3610}, headers=HEADER, timeout=20)
    assert response.json()['trainer_name'] == 'Машунька', ''