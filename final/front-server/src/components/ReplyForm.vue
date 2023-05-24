<template>
  <v-container>
    <!-- 댓글에 달린 대댓글 -->
    <div class="d-flex align-center">
      대댓글 갯수: {{ comment.replies.length }}
      <v-btn small @click="showReplies = !showReplies">접기/펼치기</v-btn>
    </div>
    <transition name="slide">
      <div v-if="showReplies">
        <v-container v-for="reply in comment.replies" :key="reply.id">
          작성자: {{ reply.user.username }} 내용: {{ reply.content }} 작성시간:
          {{ reply.created_at.slice(0, 10) }}
        </v-container>
        <v-container>
          <v-row>
            <v-text-field v-model="newreply" solo></v-text-field>
            <v-btn @click.prevent="createReply(comment.id)">작성</v-btn>
          </v-row>
        </v-container>
      </div>
    </transition>
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

<style scoped>
/* 맘에안들어 */
.slide-enter-active {
  transition: all 0.5s ease;
}
.slide-leave-active {
  transition: all 0.5s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-enter {
  transform: translateY(-20px);
  opacity: 0;
}
.slide-leave-to {
  transform: translateY(-20px);
  opacity: 0;
}
</style>
