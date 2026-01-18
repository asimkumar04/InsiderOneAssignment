import pytest
import requests

@pytest.mark.API
def test_search_pet_with_success():
    base_url = "https://petstore.swagger.io/v2/pet/findByStatus"
    para = {
        'status': 'available'
    }

    response = requests.get(base_url, params=para)
    print(response.json())
    #Assertion:
    assert response.status_code == 200  # Validation of status code

@pytest.mark.API
def test_search_pet_with_invalid_status():
    base_url = "https://petstore.swagger.io/v2/pet/findByStatus"
    para = {
        'status': 'abc'
    }
    response = requests.get(base_url, params=para)
    print(response.json())
    #Assertion:
    assert response.status_code == 400  # Validation of status code
