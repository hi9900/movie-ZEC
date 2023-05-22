<template>
<div>
  <v-btn icon @click="toggleDarkMode">
      <v-icon>mdi-theme-light-dark</v-icon>
  </v-btn>
</div>
</template>

<script>
export default {
  data: () => ({ 
      darkMode: false
    }),
    methods: {
      toggleDarkMode: function() {
        this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
        localStorage.setItem("darkTheme", this.$vuetify.theme.dark.toString())
      },
    },
}
</script>
