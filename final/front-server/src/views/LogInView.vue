<template>
  <v-container style="max-width: 450px" fill-height>
    <v-layout align-center row wrap>
      <v-flex xs12>
        <v-card>
          <div class="pa-10">
            <h1 style="text-align: center" class="mb-10">Login</h1>
            <form @submit="login">
              <!-- id -->
              <v-text-field
                label="ID"
                prepend-inner-icon="mdi-account"
                v-model="username"
              ></v-text-field>
              <!-- password -->
              <v-text-field
                prepend-inner-icon="mdi-lock"
                type="password"
                label="Password"
                v-model="password"
              >
              </v-text-field>
              <v-btn
                type="submit"
                color="blue lighten-1 text-capitalize"
                depressed
                large
                block
                dark
                class="mb-3"
              >
                Login
              </v-btn>
              <v-btn
                @click="goToSignup"
                color="blue lighten-1 text-capitalize"
                depressed
                large
                block
                dark
              >
                Sign Up
              </v-btn>
            </form>
          </div>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return{
      username: null,
      password: null,
    }
  },
  methods: {
    login(){
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }

      this.$store.dispatch('login', payload)

    },
    goToSignup() {
      this.$router.push({name: 'SignUpView'})
    }
  }
}
</script>
