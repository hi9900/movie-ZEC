<template>
  <v-container @click="goToProfile(user?.username)" class="user-row">
    <v-avatar>
      <img
        :src="`https://source.boringavatars.com/beam/40/${user?.username}`"
      />
    </v-avatar>
    {{ user?.username }}
  </v-container>
</template>

<script>
export default {
  name: 'UserProfileCard',
  props: {
    user: Object
  },
  data() {
    return {}
  },
  computed: {},
  methods: {
    goToProfile(username) {
      this.$emit('getNewProfile', username)
      console.log('usercard', username)
      // this.$router.go()
      // this.$router.push({name: 'Profile', params: {username: username}})
    }
  }
}
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
.user-row {
  display: flex;
  align-items: center;
  flex-direction: column;
  text-align: center;
  cursor: pointer;
  transition: background-color 0.3s; /* 호버 효과를 부드럽게 만듭니다. */
}
.user-avatar {
  margin-bottom: 8px;
}
.user-avatar img {
  width: 80px;
  height: 80px;
}

.user-row:hover {
  background-color: rgba(
    0,
    0,
    0,
    0.1
  ); /* 배경색 변경, 원하는 색상으로 변경하세요. */
}
</style>
