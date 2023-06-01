// @/components/ReviewForm
<template>
  <v-container>
    <!-- 댓글에 달린 대댓글 -->
    <div class="d-flex align-center">
      대댓글 갯수: {{ comment.replies.length }}
      <v-btn icon small @click="showReplies = !showReplies">
        <v-icon v-if="showReplies">mdi-chevron-up</v-icon>
        <v-icon v-else>mdi-chevron-down</v-icon>
      </v-btn>
    </div>
    <v-expand-transition>
      <div v-if="showReplies">
        <v-container v-for="reply in comment.replies" :key="reply.id">
          <div style="display: flex; justify-content: space-between">
            <div>
              <span style="font-weight: bold; margin-right: 8px">{{
                reply.user.username
              }}</span>
              <span>{{ reply.content }}</span>
            </div>
            <v-col cols="2">
              <small>{{ reply.created_at.slice(0, 10) }} 작성</small>
            </v-col>
          </div>
          <br />
        </v-container>

        <v-container>
          <v-row>
            <v-text-field
              @keyup.enter="createReply"
              v-model="newreply"
            ></v-text-field>
            <v-btn @click.prevent="createReply">작성</v-btn>
            <!-- <v-btn @click.prevent="createReply(event, comment.id)">작성</v-btn> -->
          </v-row>
        </v-container>
      </div>
    </v-expand-transition>
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
      showReplies: true
    }
  },
  methods: {
    createReply() {
      if (!this.newreply) {
        alert('내용을 입력해주세요.')
        return
      }
      const data = {
        commentId: this.comment.id,
        newreply: this.newreply
      }
      this.$emit('createReply', data)
      this.newreply = ''
    }
  }
}
</script>

<style scoped></style>
