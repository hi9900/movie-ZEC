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
        <v-btn @click="search"> 검색 </v-btn>
      </v-col>
    </v-row>

    <v-row>
      <p>{{ MoviesCount }}개의 결과</p>
    </v-row>
  </v-container>
</template>

<script>
export default {
  props: {
    searchQuery: {
      type: String,
      default: ''
    },
    MoviesCount: Number
  },
  data() {
    return {
      searchInput: this.searchQuery
    }
  },
  methods: {
    search() {
      this.$emit('search', this.searchInput)
    }
  }
}
</script>

<style>
</style>