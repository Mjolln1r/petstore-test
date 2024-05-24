import requests
from configuration import BASE_URL, HEADERS


def test_add_new_pet():
    payload = {
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

    response = requests.post(f'{BASE_URL}/pet', json=payload, headers=HEADERS)
    assert response.status_code == 200
