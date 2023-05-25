<template>
  <v-container>
    <v-form ref="form" v-model="formValid" class="form-container">
      <v-row>
        <v-col cols="12" sm="4">
          <v-text-field
            v-model="writer"
            label="이름"
            :counter="10"
            :rules="[requiredRule]"
            outlined
            small
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="4">
          <v-text-field
            v-model="password"
            label="비밀번호"
            :rules="[requiredRule]"
            type="password"
            outlined
            small
          ></v-text-field>
        </v-col>
      </v-row>

      <v-text-field
        v-model="title"
        label="제목"
        :counter="50"
        :rules="[requiredRule]"
        outlined
      ></v-text-field>
      <v-textarea
        v-model="content"
        label="내용"
        :rules="[requiredRule]"
        outlined
      ></v-textarea>
      <div class="text-right">
        <v-btn color="primary" @click="submitForm" :disabled="!formValid">
          게시글 작성
        </v-btn>
      </div>
    </v-form>
  </v-container>
</template>

<script>
// import axios from 'axios';
import {mapActions} from 'vuex'
export default {
  data() {
    return {
      formValid: false,
      writer: '',
      password: '',
      title: '',
      content: '',
      requiredRule: v => !!v || 'This field is required'
    }
  },
  methods: {
    ...mapActions('article', ['addArticle', 'getArticleList']),
    moveList() {
      this.$router.push({name: 'ArticleList'})
    },
    async submitForm() {
      const article = {
        title: this.title,
        writer: this.writer,
        password: this.password,
        content: this.content
      }
      await this.addArticle(article)
      this.getArticleList()
      this.$router.push({name: 'ArticleList'})
    }
  }
}
</script>

<style scoped>
.form-container {
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
}
</style>
