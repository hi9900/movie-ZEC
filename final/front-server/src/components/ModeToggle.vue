<template>
  <v-switch label="Dark mode" v-model="darkMode"></v-switch>
</template>

<script>
export default {
  computed: {
    darkMode: {
      get() {
        return this.$vuetify.theme.dark;
      },
      set(value) {
        this.$vuetify.theme.dark = value;
      },
    },
  },
};
</script>
