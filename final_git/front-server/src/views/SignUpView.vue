<template>
  <v-container style="max-width: 450px" fill-height>
    <v-layout align-center row wrap>
      <v-flex xs12>
        <v-card>
          <div class="pa-10">
            <h1 style="text-align: center" class="mb-10">회원가입</h1>
            <form ref="form" @submit.prevent="signUp">
              <!-- user_email -->
              <v-text-field
                label="이메일 *"
                prepend-inner-icon="mdi-email"
                v-model="user_email"
                :rules="user_email_rule"
                clearable
                required
                :error-messages="emailDuplicated ? emailDuplicatedMessage : ''"
                :messages="emailDuplicated ? emailDuplicatedMessage : ''"
                @blur="checkEmailDuplicated"
              >
              </v-text-field>

              <!-- username -->
              <v-text-field
                prepend-inner-icon="mdi-account"
                v-model="username"
                label="이름 *"
                :rules="username_rule"
                @blur="checkUsernameDuplicated"
                :error-messages="
                  usernameDuplicated ? usernameDuplicatedMessage : ''
                "
                :messages="!usernameDuplicated ? usernameDuplicatedMessage : ''"
                hint="2~10자의 문자 및 숫자만 사용 가능합니다."
                required
                clearable
              >
              </v-text-field>

              <!-- password -->
              <v-text-field
                prepend-inner-icon="mdi-lock"
                label="비밀번호 *"
                :type="show1 ? 'text' : 'password'"
                hint="8~16자 영문 대 소문자, 숫자, 특수문자를 사용하세요."
                v-model="password1"
                :rules="password_rule"
                :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append="show1 = !show1"
                clearable
                required
              ></v-text-field>
              <!-- 8~16자 영문 대 소문지, 숫자, 특수문자를 사용하세요 -->
              <v-text-field
                prepend-inner-icon="mdi-lock"
                :type="show2 ? 'text' : 'password'"
                label="비밀번호 확인"
                v-model="password2"
                :rules="password_rule2"
                :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append="show2 = !show2"
                clearable
                required
              ></v-text-field>

              <v-btn
                type="submit"
                color="text-capitalize"
                depressed
                large
                block
                dark
                class="mb-3"
              >
                회원가입
              </v-btn>
            </form>
          </div>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios'
export default {
  name: 'SignUpView',
  data() {
    return {
      show1: false,
      show2: false,
      password: 'Password',
      user_email: '',
      user_email_rule: [
        v => !!v || '이메일는 필수 입력사항입니다.',
        // 이메일 생긴거 확인하기
        v =>
          /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/.test(
            v.replace(/(\s*)/g, '')
          ) || '이메일 형식으로 입력해주세요'
      ],
      // 이름 확인
      username: '',
      username_rule: [
        v => !!v || '이름은 필수 입력사항입니다.',
        v =>
          !(v && v.length >= 11) || '2~10자의 문자 및 숫자만 사용 가능합니다.',
        v =>
          !(v && v.length <= 1) || '2~10자의 문자 및 숫자만 사용 가능합니다.',
        v =>
          !/[~!@#$%^&*()_+|<>?:{}]/.test(v) ||
          '이름에는 특수문자를 사용할 수 없습니다.'
      ],
      // 비밀번호 유효성 나중에 하기
      password1: '',
      password_rule: [
        v =>
          this.password1 === 'ins'
            ? !!v || '패스워드는 필수 입력사항입니다.'
            : true,
        v =>
          !(v && v.length >= 16) ||
          '8~16자 영문 대 소문자, 숫자, 특수문자를 사용하세요',
        v =>
          !(v && v.length <= 7) ||
          '8~16자 영문 대 소문자, 숫자, 특수문자를 사용하세요',
        v =>
          !!(v && /\d/.test(v)) ||
          '8~16자 영문 대 소문자, 숫자, 특수문자를 사용하세요',
        v =>
          !!(v && /[A-Za-z]/.test(v)) ||
          '8~16자 영문 대 소문자, 숫자, 특수문자를 사용하세요',
        v =>
          !!(v && /[^A-Za-z0-9]/.test(v)) ||
          '8~16자 영문 대 소문자, 숫자, 특수문자를 사용하세요',
        v =>
          !!(v && /[A-Z]{1}/.test(v)) ||
          '8~16자 영문 대 소문자, 숫자, 특수문자를 사용하세요'
      ],
      password2: '',
      password_rule2: [
        v =>
          this.password2 === 'ins'
            ? !!v || '패스워드는 필수 입력사항입니다.'
            : true,
        v => v === this.password1 || '패스워드가 일치하지 않습니다.'
      ],
      usernameDuplicated: false,
      usernameDuplicatedMessage: '',
      emailDuplicated: false,
      emailDuplicatedMessage: ''
    }
  },
  methods: {
    signUp() {
      console.log('signup')
      const email = this.user_email
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        email,
        username,
        password1,
        password2
      }

      this.$store.dispatch('account/signUp', payload)
    },

    async checkUsernameDuplicated() {
      const API_URL = 'http://127.0.0.1:8000'
      if (this.username) {
        try {
          const response = await axios.get(
            `${API_URL}/accounts/check-username/${this.username}/`
          )
          this.usernameDuplicated = !response.data.result
          this.usernameDuplicatedMessage = response.data.message
        } catch (error) {
          console.error('Error during username checking:', error)
        }
      }
    },
    async checkEmailDuplicated() {
      const API_URL = 'http://127.0.0.1:8000'
      if (this.user_email) {
        try {
          const response = await axios.get(
            `${API_URL}/accounts/check-email/${this.user_email}/`
          )
          this.emailDuplicated = !response.data.result
          this.emailDuplicatedMessage = response.data.message
        } catch (error) {
          console.error('Error during email checking:', error)
        }
      }
    }
  }
}
</script>
