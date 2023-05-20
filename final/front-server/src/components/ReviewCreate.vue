<!-- src/components/ReviewForm.vue -->
<template>
  <v-container>
    <v-row>
      <v-col cols="12" md="8">
        <!-- 영화 이미지 및 제목 -->
      </v-col>
      <v-col cols="12" md="4">
        <v-card class="mx-auto mt-10">
          <v-card-title>리뷰 작성하기</v-card-title>
          <v-card-text>
            <v-form ref="form" v-model="valid" @submit.prevent="submit">
              <v-text-field
                v-model="user"
                label="작성자 이름"
                :counter="20"
                :rules="[rules.required]"
                required
              ></v-text-field>
              <v-textarea
                v-model="review"
                label="리뷰 내용"
                :rules="[rules.required, rules.contentLength]"
                outlined
                required
                clearable
                clear-icon="mdi-close-circle-outline"
              ></v-textarea>
              <v-btn type="submit" color="primary">리뷰 작성하기</v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      valid: true,
      user: "",
      review: "",
      rules: {
        required: value => !!value || "필수 입력 사항입니다.",
        contentLength: value =>
          value.length >= 25 || "리뷰 내용은 최소 25자 이상이어야합니다."
      }
    };
  },
  methods: {
    submit() {
      if (this.$refs.form.validate()) {
        alert("리뷰가 저장되었습니다.");
        this.$refs.form.reset();
        this.valid = false;
      } else {
        alert("입력값을 확인해주세요.");
      }
    }
  }
};
</script>
