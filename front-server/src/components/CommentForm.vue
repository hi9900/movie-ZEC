<template>
  <v-card>
    <v-card-text>
      <v-text-field
        v-model="newComment"
        label=""
        @keyup.enter="createComment"
        rows="1"
      />
    </v-card-text>
    <v-card-actions>
      <v-btn color="primary" @click.prevent="createComment">작성</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      newComment: ''
    }
  },
  methods: {
    // creatComment() {
    //   const data = {
    //     newComment
    //   }
    //   this.$emit('')
    // }
  }
}
</script>

<style>
</style>