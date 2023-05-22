<template>
<v-container>
  <v-row>
      <v-col cols="10">
      <!-- 여긴 검색창 -->
      <v-text-field
      v-model="searchInput"
      label="Search for movies"
      @keyup.enter="search"
      prepend-inner-icon="mdi-magnify"
      outlined
      filled
      rounded
      dense
    >
    </v-text-field>
    </v-col>

      <v-col cols="2">
      <!-- 검색버튼 -->
        <v-btn @click="search">
          검색
        </v-btn>
      </v-col>
    </v-row>


    <!-- <v-row>
    <v-btn @click="filterData">Filter Data</v-btn>
    <v-select
      label="Filter by"
      v-model="selectedFilter"
      :items="filters"
      item-text="text"
      item-value="value"
    ></v-select>
    <v-text-field label="Filter value" v-model="filterValue"></v-text-field>
    </v-row> -->

    <v-row>
      <p>{{ MoviesCount }}개의 결과</p>
    </v-row> 
    </v-container>
</template>

<script>
// import { mapActions } from 'vuex'
export default {
   props: {
    searchQuery: {
      type: String,
      default: '',
    },
    MoviesCount: Number,
   },
  data() {
    return {
     searchInput: this.searchQuery,
    }
  },
  methods: {
    search() {
      this.$emit('search', this.searchInput)
    },
    // ...mapActions(['movie/filterMovies']),
    // filterMovies() {
    //   let filter;
    //   switch (this.filter) {
    //     case "rating":
    //       filter = `vote_average:${this.query}`;
    //       break;
    //     case "genre":
    //       filter = `genres__name:${this.query}`;
    //       break;
    //     case "keyword":
    //       filter = `keywords__name:${this.query}`;
    //       break;
    //     case "director":
    //       filter = `director__name:${this.query}`;
    //       break;
    //     case "year":
    //       filter = `release_date:${this.query}`;
    //       break;
    //   }
    //   this.filterMovies(filter);
    // },
  }
}
</script>

<style>

</style>