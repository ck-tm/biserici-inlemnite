import requests
from pprint import pprint

body = {
    # "advanced": {
    # #     "descriere": {
    # #         "amplasament": [1]
    # #     },
    #     "conservare": {
    #         "sit": [2,3,5]
    #     }
    # }, 
    "basic": {
        # "judet": [3],
        # "localitate": [1],
        "conservare": [
            3
        ],
        "valoare": [
            2
        ],
        "prioritizare": [
            2,
        ]
    }
}

url = 'http://localhost:8000/api/map/filter/'
r = requests.post(url, json=body)
pprint(r.json())


