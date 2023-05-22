<template>
  <v-container>
    <v-row>
      <v-col v-for="list in movieLists" :key="list.id" cols="12" sm="6" md="4">
        <v-card>
          <v-card-title>{{ list.title }}</v-card-title>
          <v-card-text>
              <div class="poster-container">
              <v-img
                v-for="(movie, index) in list.movies.slice(0, 5)"
                :key="movie.id"
                :src="movie.poster"
                :alt="movie.title"
                class="poster"
                :style="{ zIndex: list.movies.length - index, marginLeft: -index * 20 + 'px' }"
              ></v-img>
            </div>
              <v-col v-if="list.movies.length > 5" cols="4" class="more-movies">
                <v-chip>+{{ list.movies.length - 5 }}</v-chip>
              </v-col>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'MovieLists',
  data() {
    return {
      // 샘플 데이터, 실제로는 서버에서 가져올 것입니다.
      // 각 리스트에서 최근에 추가된 5개 영화의 포스터 를 계산해서 가져오기
      movieLists: [
        {
          id: 1,
          title: '리스트 1',
          movies: [
            { id: 1, title: '영화 1', poster: 'https://image.tmdb.org/t/p/w342/glrBsRe2SzcL1dNgayNkr6Okbkm.jpg' },
            { id: 1, title: '영화 1', poster: 'https://image.tmdb.org/t/p/w342/glrBsRe2SzcL1dNgayNkr6Okbkm.jpg' },
            { id: 1, title: '영화 1', poster: 'https://image.tmdb.org/t/p/w342/glrBsRe2SzcL1dNgayNkr6Okbkm.jpg' },
            { id: 1, title: '영화 1', poster: 'https://image.tmdb.org/t/p/w342/glrBsRe2SzcL1dNgayNkr6Okbkm.jpg' },
            { id: 1, title: '영화 1', poster: 'https://image.tmdb.org/t/p/w342/glrBsRe2SzcL1dNgayNkr6Okbkm.jpg' },
            // ...
          ],
        },
        {
          id: 2,
          title: '리스트 1',
          movies: [
            { id: 1, title: '영화 1', poster: 'https://image.tmdb.org/t/p/w342/glrBsRe2SzcL1dNgayNkr6Okbkm.jpg' },
            { id: 1, title: '영화 1', poster: 'https://image.tmdb.org/t/p/w342/glrBsRe2SzcL1dNgayNkr6Okbkm.jpg' },
            { id: 1, title: '영화 1', poster: 'https://image.tmdb.org/t/p/w342/glrBsRe2SzcL1dNgayNkr6Okbkm.jpg' },
            { id: 1, title: '영화 1', poster: 'https://image.tmdb.org/t/p/w342/glrBsRe2SzcL1dNgayNkr6Okbkm.jpg' },
            { id: 1, title: '영화 1', poster: 'https://image.tmdb.org/t/p/w342/glrBsRe2SzcL1dNgayNkr6Okbkm.jpg' },
            // ...
          ],
        },
        // ...
      ],
    };
  },
};
</script>

<style>
.poster-container {
  display: flex;
  align-items: flex-start;
}

.poster {
  width: 100px;
  height: auto;
  object-fit: cover;
}
.more-movies {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
}
</style>
