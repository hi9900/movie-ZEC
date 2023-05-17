import requests
from pprint import pprint

# https://developer.themoviedb.org/reference/movie-popular-list
url = "https://api.themoviedb.org/3/movie/popular?page=1"

headers = {"accept": "application/json"}

# range 범위 받고 싶은 만큼 바꿔야함 최대 500이었나
for p in range(1, 2):
    params = {
        'api_key': '3a4accd7ba8d3add19c510122c8c1b72',
        'language': 'ko-KR',
        'page': f'{p}'
    }

    data = requests.get(url, headers=headers, params=params).json()
    # print(data['results'][0].keys())

    # pprint(data['results'][0])
    # print(p, len(data['results']))

    # 한페이지 최대 20개
    # pages = len(data['results'])
    pages = 1
    for i in range(pages):

        movie_id = data['results'][i]['id']
        detail_url = f'https://api.themoviedb.org/3/movie/{movie_id}'
        params = {
            'api_key': '3a4accd7ba8d3add19c510122c8c1b72',
            'language': 'ko-KR',
        }

        response = requests.get(detail_url, headers=headers, params=params).json()

        # pprint(response)
        # print(response.keys())
        print('#'*100)

        # credits
        credits_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
        response = requests.get(credits_url, headers=headers, params=params).json()
        # 배우
        # pprint(response['cast'])

        # pprint(response['crew'])
        # 감독(director)
        for j in range(len(response['crew'])):
            if response['crew'][j]['job'] == 'Director':
                pprint(response['crew'][j])
        print('#'*100)
        # 키워드
        keywords_url = f'https://api.themoviedb.org/3/movie/{movie_id}/keywords'
        response = requests.get(keywords_url, headers=headers, params=params).json()
        pprint(response)
        print('#'*100)

        # TMDB 선정 추천영화 
        recommendations_url = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'
        params = {
            'api_key': '3a4accd7ba8d3add19c510122c8c1b72',
            'language': 'ko-KR',
        }
        response = requests.get(recommendations_url, headers=headers, params=params).json()
        pprint(response)
        for j in range(len(response['results'])):
            print(response['results'][j]['id'])

