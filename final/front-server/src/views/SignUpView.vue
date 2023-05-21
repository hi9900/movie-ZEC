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
                label="이메일*"
                prepend-inner-icon="mdi-email"
                v-model="user_email"
                :rules="user_email_rule"
              >
              <!-- 포커스를 잃으면 중복 확인 API가 호출되고 중복 여부에 따라 표시가 표시 -->
              <!-- <v-text-field
              label="이메일"
              v-model="email"
              :error-messages="emailDuplicated ? emailDuplicatedMessage : ''"
              @blur="checkEmailDuplicated"
            > -->
              </v-text-field>
              <v-text-field 
                prepend-inner-icon="mdi-account"
                v-model="username" 
                label="이름*" 
                :rules="username_rule" 
                required
                >
                <!-- <v-text-field
                label="닉네임"
                v-model="nickname"
                :error-messages="nicknameDuplicated ? nicknameDuplicatedMessage : ''"
                @blur="checkNicknameDuplicated"
              > -->
                </v-text-field>

              
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
      user_email_rule: [
        v => !!v || '이메일는 필수 입력사항입니다.',
        v => /^[a-zA-Z0-9]*$/.test(v) || '아이디는 영문+숫자만 입력 가능합니다.',
        // 아이디 중복 확인
        v => this.checkDuplicate(v)
      ],
      username: '',
      username_rule: [
        v => !!v || '이름은 필수 입력사항입니다.',
        v => !(v && v.length >= 30) || '이름은 10자 이상 입력할 수 없습니다.',
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
    //   nicknameDuplicated: false,
    // nicknameDuplicatedMessage: '',
    // emailDuplicated: false,
    // emailDuplicatedMessage: '',
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
    },
    // 일단 긁어왔는데 되는지는 몰라서 주석
  //   async checkNicknameDuplicated() {
  //   if (this.nickname) {
  //     try {
  //       const response = await axios.get(`/api/check-nickname/${this.nickname}`);
  //       this.nicknameDuplicated = !response.data.result;
  //       this.nicknameDuplicatedMessage = response.data.message;
  //     } catch (error) {
  //       console.error('Error during nickname checking:', error);
  //     }
  //   }
  // },
  // async checkEmailDuplicated() {
  //   if (this.email) {
  //     try {
  //       const response = await axios.get(`/api/check-email/${this.email}`);
  //       this.emailDuplicated = !response.data.result;
  //       this.emailDuplicatedMessage = response.data.message;
  //     } catch (error) {
  //       console.error('Error during email checking:', error);
  //     }
  //   }
  // },
  }
}
</script>
