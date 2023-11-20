import requests
from pprint import pprint

# TMDB url
URL = f"https://api.themoviedb.org/3/"


URL_genre = 'https://api.themoviedb.org/3/genre/movie/list'

params = {
'api_key': '3a4accd7ba8d3add19c510122c8c1b72',
'language': 'ko-KR',
}

response = requests.get(URL_genre, params=params).json()
print(response)


url = f"https://api.themoviedb.org/3/person/popular"

params = {
    'api_key': '3a4accd7ba8d3add19c510122c8c1b72',
    'language': 'ko-KR',
    'page': 1,
}

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers, params=params).json()

pprint(response)