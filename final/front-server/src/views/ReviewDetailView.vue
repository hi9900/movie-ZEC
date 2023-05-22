<template>
  <v-app>
    <v-container>
      <v-row>
        <v-col cols="12" md="8">
          <!-- 영화 포스터, 제목 적기 -->
          <!-- 누르면 영화 상세 페이지로 -->
          <movie-detail :movie="movie" />

          <!-- 리뷰 내용: 작성자, 리뷰 날짜, 리뷰 내용, 별점 -->
          <review v-for="review in reviews" :key="review.id" :review="review" />

          <v-card>
            <v-card-title>Leave a comment</v-card-title>
            <v-card-text>
              <v-textarea v-model="newComment" label="Your comment" />
            </v-card-text>
            <v-card-actions>
              <v-btn color="primary" @click="leaveComment">Submit</v-btn>
            </v-card-actions>
          </v-card>
          <!-- 로그인 시 작성할 수 있게 -->

          <!-- 리뷰에 달린 댓굴 -->
          <comment
            v-for="comment in comments"
            :key="comment.id"
            :comment="comment"
          />
        </v-col>

        <v-col cols="12" md="4">
          <profile-card :profile="profile" />
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
// import MovieDetail from "@/components/MovieDetail.vue";
// import Rating from "@/components/Rating.vue";
// import Review from "@/components/Review.vue";
// import Comment from "@/components/Comment.vue";
// import ProfileCard from "@/components/ProfileCard.vue";

export default {
  components: {
    // MovieDetail,
    // Rating,
    // Review,
    // Comment,
    // ProfileCard
  },
  data() {
    return {
      movie: {
        title: "The Super Mario Bros Movie",
        year: "1993",
        description: "Film description",
        poster: "/path/to/poster.jpg"
      },
      reviews: [
        {
          id: 1,
          author: { username: "username1" },
          content: "This movie is great!",
          rating: 4
        },
        {
          id: 2,
          author: { username: "username2" },
          content: "I love this movie!",
          rating: 5
        }
      ],
      comments: [
        { id: 1, author: { username: "username1" }, content: "I agree!" },
        { id: 2, author: { username: "username2" }, content: "Me too!" }
      ],
      newComment: "",
      profile: {
        name: "Profile Name",
        username: "ProfileUsername",
        avatar: "/path/to/avatar.jpg"
      }
    };
  },
  methods: {
    leaveComment() {
      const newCommentObj = {
        id: this.comments.length + 1,
        author: { username: "User3" },
        content: this.newComment
      };
      this.comments.push(newCommentObj);
      this.newComment = "";
    }
  }
};
</script>
