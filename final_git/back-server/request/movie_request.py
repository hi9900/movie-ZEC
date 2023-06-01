import requests
from pprint import pprint

f = open('movies_movie.csv', 'w', encoding='utf-8')
f.write('id,title,original_language,original_title,overview,release_date,popularity,vote_count,vote_average,poster_path,backdrop_path,runtime'+'\n')
f.close()
f = open('movies_actor.csv', 'w', encoding='utf-8')
f.write('id,name,profile_path'+'\n')
# f.write('id,character,name,profile_path'+'\n')
f.close()
f = open('movies_director.csv', 'w', encoding='utf-8')
f.write('id,name,profile_path'+'\n')
f.close()
f = open('movies_keyword.csv', 'w', encoding='utf-8')
f.write('id,name'+'\n')
f.close()

f = open('movies_character.csv', 'w', encoding='utf-8')
f.write('pk,character,movie_id,actor_id'+'\n')
character_pk = 1
f.close()
f = open('movies_movie_director.csv', 'w', encoding='utf-8')
f.write('pk,movie_id,director_id'+'\n')
movie_director_pk = 1
f.close()
f = open('movies_movie_genres.csv', 'w', encoding='utf-8')
f.write('pk,movie_id,genre_id'+'\n')
movie_genres_pk = 1
f.close()
f = open('movies_movie_keywords.csv', 'w', encoding='utf-8')
f.write('pk,movie_id,keyword_id'+'\n')
movie_keywords_pk = 1
f.close()

# https://developer.themoviedb.org/reference/movie-popular-list
url = "https://api.themoviedb.org/3/movie/popular"
headers = {"accept": "application/json"}

# range 범위 받고 싶은 만큼 바꿔야함 최대 500이었나

for p in range(1, 500):
    print(p)
    params = {
        'api_key': '3a4accd7ba8d3add19c510122c8c1b72',
        'language': 'ko-KR',
        'page': f'{p}'
    }

    data = requests.get(url, headers=headers, params=params).json()
    
    # print(data['results'][0].keys())

    # pprint(data['results'])
    # print(p, len(data['results']))


    # 한페이지 최대 20개
    pages = len(data['results'])
    # pages = 1
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
######################################################################
        movie_id = movie_id
        title = response['title'].replace(',', '')
        original_language = response['original_language']
        original_title = response['original_title'].replace(',', '')
        overview = response['overview'].replace(',', '').replace('\r', '').replace('\n', '')
        release_date = response['release_date']
        popularity = response['popularity']
        vote_count = response['vote_count']
        vote_average = response['vote_average']
        poster_path = response['poster_path']
        backdrop_path = response['backdrop_path']
        runtime = response['runtime']

        # f = open('movies_movie.csv', 'w', encoding='utf-8')
        f = open('movies_movie.csv', 'a', encoding='utf-8')
        f.write(f'{movie_id},{title},{original_language},{original_title},{overview},{release_date},{popularity},{vote_count},{vote_average},{poster_path},{backdrop_path},{runtime}'+'\n')
        f.close()
######################################################################

        # pprint(response['genres'])
        f = open('movies_movie_genres.csv', 'a', encoding='utf-8')
        for j in range(len(response['genres'])):
            # print(response['genres'][j]['id'])
            genre_id = response['genres'][j]['id']
            f.write(f'{movie_genres_pk},{movie_id},{genre_id}'+'\n')
            movie_genres_pk += 1
        f.close()

        # print('#'*100)
######################################################################

        # credits
        credits_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
        response = requests.get(credits_url, headers=headers, params=params).json()
        # 배우
        # pprint(response['cast'])
        f = open('movies_actor.csv', 'a', encoding='utf-8')
        f2 = open('movies_character.csv', 'a', encoding='utf-8')
        for j in range(len(response['cast'])):
            id = response['cast'][j]['id']
            character = response['cast'][j]['character'].replace(',', '').replace('"', '')
            name = response['cast'][j]['name'].replace(',', '')
            profile_path = response['cast'][j]['profile_path']

            f.write(f'{id},{name},{profile_path}'+'\n')
            f2.write(f'{character_pk},{character},{movie_id},{id}'+'\n')
            character_pk += 1
        f.close()
        f2.close()
######################################################################

        # pprint(response['crew'])
        # 감독(director)
        f = open('movies_director.csv', 'a', encoding='utf-8')
        f2 = open('movies_movie_director.csv', 'a', encoding='utf-8')

        for j in range(len(response['crew'])):
            if response['crew'][j]['job'] == 'Director':
                # pprint(response['crew'][j])
                id = response['crew'][j]['id']
                name = response['crew'][j]['name'].replace(',', '')
                profile_path = response['crew'][j]['profile_path']
                f.write(f'{id},{name},{profile_path}'+'\n')
                f2.write(f'{movie_director_pk},{movie_id},{id}'+'\n')
                movie_director_pk += 1
        f.close()
        f2.close()
        # print('#'*100)
######################################################################


        # 키워드
        keywords_url = f'https://api.themoviedb.org/3/movie/{movie_id}/keywords'
        response = requests.get(keywords_url, headers=headers, params=params).json()
        # 키워드에 id, name 넣고
        # 중개 테이블에 movieid, keywordid 넣고
        # pprint(response['keywords'])
        f = open('movies_keyword.csv', 'a', encoding='utf-8')
        f2 = open('movies_movie_keywords.csv', 'a', encoding='utf-8')
        for j in range(len(response['keywords'])):
            id = response['keywords'][j]['id']
            name = response['keywords'][j]['name'].replace(',', '')
            f.write(f'{id},{name}'+'\n')
            f2.write(f'{movie_keywords_pk},{movie_id},{id}'+'\n')
            movie_keywords_pk += 1
        f.close()
        f2.close()
        # print('#'*100)

        # # TMDB 선정 추천영화 
        # recommendations_url = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'
        # params = {
        #     'api_key': '3a4accd7ba8d3add19c510122c8c1b72',
        #     'language': 'ko-KR',
        # }
        # response = requests.get(recommendations_url, headers=headers, params=params).json()
        # pprint(response)
        # for j in range(len(response['results'])):
        #     print(response['results'][j]['id'])

