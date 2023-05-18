import requests
from pprint import pprint


url = "https://api.themoviedb.org/3/configuration/languages"

headers = {"accept": "application/json"}

params = {
    'api_key': '3a4accd7ba8d3add19c510122c8c1b72',
    }

response = requests.get(url, headers=headers, params=params).json()

pprint(response)