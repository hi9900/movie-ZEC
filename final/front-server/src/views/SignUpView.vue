<template>
  <v-container style="max-width: 450px" fill-height>
    <v-layout align-center row wrap>
      <v-flex xs12>
        <v-card>
          <div class="pa-10">
            <h1 style="text-align: center" class="mb-10">회원가입</h1>
            <form ref="form">
              <!-- id -->
              <v-text-field
                label="아이디*"
                prepend-inner-icon="mdi-account"
                v-model="user_id"
                :rules="user_id_rule"
              ></v-text-field>
              <v-text-field 
                prepend-inner-icon="mdi-account"
                v-model="username" 
                label="이름*" 
                :rules="username_rule" 
                required
                ></v-text-field>

              <!-- email 나중에 찾아서 -->
              <!-- <v-text-field
                label="E-mail"
                prepend-inner-icon="mdi-email"
                v-model="email"
              ></v-text-field> -->
              
              <!-- password -->
              <v-text-field 
                prepend-inner-icon="mdi-lock"
                label="비밀번호*" 
                type="password1" 
                v-model="password1"
                :rules="password_rule"
                ></v-text-field>
              <v-text-field
                prepend-inner-icon="mdi-lock"
                type="password2"
                label="비밀번호 확인*"
                v-model="password2"
                :rules="password_rule2"
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
                Signup
              </v-btn>
            </form>
          </div>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
  <!-- <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      
      <input type="submit" value="SignUp">
    </form>
  </div> -->
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return{
      user_id: '',
      user_id_rule: [
        v => !!v || '아이디는 필수 입력사항입니다.',
        v => /^[a-zA-Z0-9]*$/.test(v) || '아이디는 영문+숫자만 입력 가능합니다.',
        // 아이디 중복 확인
        v => this.checkDuplicate(v)
      ],
      username: '',
      username_rule: [
        v => !!v || '이름은 필수 입력사항입니다.',
        v => !(v && v.length >= 30) || '이름은 30자 이상 입력할 수 없습니다.',
        v => !/[~!@#$%^&*()_+|<>?:{}]/.test(v) || '이름에는 특수문자를 사용할 수 없습니다.'
      ],
      password1: '',
      password2: '',
      password_rule: [
        v => this.state === 'ins' ? !!v || '패스워드는 필수 입력사항입니다.' : true,
        v => !(v && v.length >= 30) || '패스워드는 30자 이상 입력할 수 없습니다.',
      ],
      password_rule2: [
        v => this.state === 'ins' ? !!v || '패스워드는 필수 입력사항입니다.' : true,
        v => !(v && v.length >= 30) || '패스워드는 30자 이상 입력할 수 없습니다.',
        v => v === this.user_pw || '패스워드가 일치하지 않습니다.'
      ],
      email: null,
    }
  },
  methods: {
    signUp() {
      // console.log('signup')
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2
      }

      this.$store.dispatch('signUp', payload)
    },
    checkDuplicate(user_id) {
      const user_data = this.$store.getters['setting/user/GET_USER_LIST']

      for(let i in user_data) {
        let user_idcheck = user_data[i].user_id
        if (user_id === user_idcheck){
          return '이미 사용중인 아이디입니다.'
        }
      }
      return true
    }
  }
}
</script>
