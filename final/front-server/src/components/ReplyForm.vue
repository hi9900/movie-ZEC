<template>
  <v-container>
    <!-- 댓글에 달린 대댓글 -->
          대댓글 갯수: {{ comment.replies.length }}
        <v-container v-for="reply in comment.replies" :key="reply.id">
          작성자: {{ reply.user }}
          내용: {{ reply.content }}
          작성시간: {{ reply.created_at }}
        </v-container>
        <v-container>
          <v-btn >대댓글 쓰기</v-btn>
          <!-- 대댓글쓰기 버튼을 누르면 보이게하고 대댓글버튼은 사라지게 -->
          <v-row>
          <v-text-field 
            v-model="newreply"
            solo></v-text-field>
          <v-btn @click.prevent="createReply(comment.id)">작성</v-btn>
          </v-row>
        </v-container>
  </v-container>
</template>

<script>
export default {
  props: {
    comment: Object
  },
  data() {
    return {
      newreply: '',
    }
  },
  methods: {
    createReply(commentId) {
      const data = {
        commentId,
        newreply: this.newreply
      }
      this.$emit('createReply', data)
      this.newreply = ''
    }
  }
}
</script>

<style>

</style>