<template>
  <v-container style="max-width: 450px" fill-height>
    <v-layout align-center row wrap>
      <v-flex xs12>
        <v-card>
          <div class="pa-10">
            <h1 style="text-align: center" class="mb-10">로그인</h1>
            <form @submit.prevent="login">
              <!-- id -->
              <v-text-field
                label="이메일"
                prepend-inner-icon="mdi-email"
                v-model="user_email"
                clearable
                required
                @blur="checkEmailDuplicated"
                :error-messages="!emailDuplicated ? '존재하지 않는 이메일입니다.' : ''"
              >
              </v-text-field>

              <!-- password -->
              <v-text-field 
                prepend-inner-icon="mdi-lock"
                label="비밀번호" 
                type="password" 
                v-model="password"
                clearable
                required
                ></v-text-field>

              <v-btn
                type="submit"
                color="blue lighten-1 text-capitalize"
                depressed
                large
                block
                dark
                class="mb-3"
              >
                로그인
              </v-btn>
              
              <v-btn
                @click="goToSignup"
                color="blue lighten-1 text-capitalize"
                depressed
                large
                block
                dark
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
  name: 'LogInView',
  data() {
    return{
      user_email: null,
      password: null,
      
      emailDuplicated: true,
      emailDuplicatedMessage: '',
    }
  },
  methods: {
    login(){
      const email = this.user_email
      const password = this.password

      const payload = {
        email, password
      }

      this.$store.dispatch('account/login', payload)

    },
    goToSignup() {
      this.$router.push({name: 'SignUp'})
    },
    async checkEmailDuplicated() {
    const API_URL = 'http://127.0.0.1:8000' 
    if (this.user_email) {
      try {
        const response = await axios.get(`${API_URL}/accounts/check-email/${this.user_email}`);
        this.emailDuplicated = !response.data.result
        this.emailDuplicatedMessage = response.data.message
      } catch (error) {
        console.error('Error during email checking:', error)
      }
    }
  },
  }
}
</script>
