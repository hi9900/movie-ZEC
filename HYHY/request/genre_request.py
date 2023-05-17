import requests
from pprint import pprint


url = "https://api.themoviedb.org/3/genre/movie/list"

headers = {"accept": "application/json"}

params = {
    'api_key': '3a4accd7ba8d3add19c510122c8c1b72',
    'language': 'ko-KR',
}

data = requests.get(url, headers=headers, params=params).json()

# pprint(response['genres'])
# pprint(len(response['genres']))
# drf 생성 POST 요청 경로
api_url = f'http://127.0.0.1:8000/api/v1/genres/'
nums = len(data['genres'])


# for i in range(nums):
    # print(i, data['genres'][i])

    # id = int(data['genres'][i]['id'])
    # name = data['genres'][i]['name']
    # # print(id, name)
    # response = requests.post(api_url, data={'id': id, 'name': name})
    # print(response)

f = open('genre.csv', 'w', encoding='utf-8')
f.write(f'id,name'+'\n')
for i in range(nums):
    id = int(data['genres'][i]['id'])
    name = data['genres'][i]['name']
    
    f.write(f'{id},{name}'+'\n')

f.close()