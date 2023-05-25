<template>
  <form action="">
    <v-text-field v-model="title" type="text" label="title"></v-text-field>
    <v-text-field v-model="writer" type="text" label="writer"></v-text-field>
    <v-text-field
      v-model="password"
      type="text"
      label="password"
    ></v-text-field>
    <v-text-field v-model="content" type="text" label="content"></v-text-field>
    <v-btn @click="create">생성</v-btn>
  </form>
</template>

<script>
export default {
  data() {
    return {
      title: '',
      writer: '',
      password: '',
      content: ''
    }
  },
  methods: {
    create() {
      // 게시글 생성 axios요청으로
      // data에 저거 담아서
      // 보내기
      // then -> articleList로
    }
  }
}
</script>

<style></style>
