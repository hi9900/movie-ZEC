<template>
  <v-card outlined>
    <v-list-item>
      <v-list-item-avatar>
        <img :src="user.profileImage" alt="프로필 이미지" />
      </v-list-item-avatar>
      <v-list-item-content>
      <v-col>
        <v-list-item-title>
          <router-link :to="`/profile/${user.username}`">{{ user.username }}</router-link>
        </v-list-item-title>
        <p class="follow-info">{{ user.followers || 0 }} 팔로워 · {{ user.following || 0 }} 팔로잉</p>
        </v-col>
        <v-row>
          <v-col>
            <v-icon color="grey">mdi-eye</v-icon>
            <span class="review-info">{{ user.review || 0 }} 리뷰갯수</span>
          </v-col>
          <v-col>
            <v-icon color="grey">mdi-comment-outline</v-icon>
            <span class="review-info">{{ user.list || 0 }} 리스트 갯수</span>
          </v-col>
          <v-col>
            <v-icon color="grey">mdi-thumb-up</v-icon>
            <span class="review-info">{{ user.likes || 0 }} 좋아요 갯수</span>
          </v-col>
        </v-row>
      </v-list-item-content>
      <v-list-item-action>
        <v-btn @click="follow" color="primary">팔로우</v-btn>
      </v-list-item-action>
    </v-list-item>
  </v-card>
</template>

<script>
export default {
  name: "UserProfileCard",
  props: {
    user: Object,
  },
  methods: {
    follow() {
      // 팔로우 버튼 클릭 시 실행됩니다
    },
  },
};
</script>

<style scoped>
.follow-info {
  font-size: 14px;
  color: #9e9e9e;
}

.review-info {
  font-size: 14px;
  color: #9e9e9e;
}
</style>
