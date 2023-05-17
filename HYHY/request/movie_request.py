import requests
from pprint import pprint

# https://developer.themoviedb.org/reference/movie-popular-list
url = "https://api.themoviedb.org/3/movie/popular?page=1"

headers = {"accept": "application/json"}

for p in range(1, 2):
    params = {
        'api_key': '3a4accd7ba8d3add19c510122c8c1b72',
        'language': 'ko-KR',
        'page': f'{p}'
    }

    data = requests.get(url, headers=headers, params=params).json()
    print(data['results'][0].keys())

    # pprint(data['results'][0])
    # print(p, len(data['results']))

    # 한페이지 최대 20개
    # pages = len(data['results'])
    pages = 1
    for i in range(pages):

        movie_id = data['results'][i]['id']
        detail_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        params = {
            'api_key': '3a4accd7ba8d3add19c510122c8c1b72',
            'language': 'ko-KR',
        }
        headers = {"accept": "application/json"}

        response = requests.get(detail_url, headers=headers, params=params).json()

        # pprint(response)
        print(response.keys())