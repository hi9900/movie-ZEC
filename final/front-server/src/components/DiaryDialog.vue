<!-- DiaryDialog.vue -->
<template>
  <v-dialog v-model="value" max-width="600">
    <v-card>
      <v-card-title>{{ entry.title }}</v-card-title>
      <v-card-text>{{ entry.date }}<br />{{ entry.content }}</v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="value = false">닫기</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script scoped>
export default {
  name: 'DiaryDialog',
  props: {
    value: Boolean,
    entry: Object,
  },
};
</script>
