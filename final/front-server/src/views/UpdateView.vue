<template>
  <div>
    <h1>회원정보 수정</h1>

    <!-- 8~16자 영문 대 소문지, 숫자, 특수문자를 사용하세요 -->
    <v-text-field
      prepend-inner-icon="mdi-lock"
      :type="show2 ? 'text' : 'password'"
      label="비밀번호 확인"
      v-model="password"
      :rules="password_rule2"
      :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
      @click:append="show2 = !show2"
      clearable
      required
    ></v-text-field>

    <v-btn @click="UpdatePassword">비밀번호 변경</v-btn>
  </div>
</template>

<script>
export default {
  data() {
    return {
      password: ''
    }
  },
  methods: {
    UpdatePassword() {
      this.$store.dispatch('account/UpdatePassword')
    }
  }
}
</script>

<style>
</style>