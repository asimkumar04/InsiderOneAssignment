from email import header

import pytest
import requests

@pytest.mark.API
def test_add_pet_with_success():

    header = {
       'Accept': 'application/json',
       'Content-Type': 'application/json'
    }
    request_payload= {
        "id": 0,
        "category": {
        "id": 0,
        "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
        "string"
        ],
        "tags": [
        {
        "id": 0,
        "name": "string"
        }
        ],
        "status": "available"
    }
    base_url = "https://petstore.swagger.io/v2/pet"
    response = requests.post(base_url,
                             headers=header,
                             json=request_payload)
    print(response.json())
    #Assertion:
    data = response.json()
    print(data["id"])
    assert response.status_code == 200  # Validation of status code

@pytest.mark.API
def test_add_pet_with_invalid_data():

    header = {
       'Accept': 'application/json',
       'Content-Type': 'application/json'
    }
    request_payload= {
        "id": 0,
        "category": {
        "id": 0,
        "name": 12345678
        },
        "name": "doggie",
        "photoUrls": [
        "string"
        ],
        "tags": [
        {
        "id": 0,
        "name": "string"
        }
        ],
        "status": "available"
    }
    base_url = "https://petstore.swagger.io/v2/pet"
    response = requests.post(base_url,
                             headers=header,
                             json=request_payload)
    print(response.json())
    #Assertion:
    data = response.json()
    print(data["id"])
    assert response.status_code == 400  # Validation of status code