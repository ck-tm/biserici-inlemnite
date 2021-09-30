import requests
from pprint import pprint

body = [
    {
        "descriere": [{
            "key": "amplasament",
            "values": [1]
        }],
    },
    {
        "conservare": [{
            "key": "sit",
            "values": [3,5]
        }]
    }
]

url = 'http://localhost:8000/api/map/filter/'
r = requests.post(url, json=body)
pprint(r.json())


