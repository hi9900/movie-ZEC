<template>
  <v-skeleton-loader v-if="!review"></v-skeleton-loader>
  <v-container v-else>
      <v-row>
        <v-col>
          <!-- 영화 포스터, 제목 적기 -->
          <!-- 누르면 영화 상세 페이지로 -->
          <!-- <movie-detail :movie="movie" /> -->

          <p>영화 정보: {{review?.movie}} -> 무비 pk임 무비디테일로 보내?</p>
        </v-col>
        <v-col>
          
          <p>작성자 pk: {{review?.user}} -> 작성자 유저네임 알아오기</p>
          <p>리뷰 내용: {{review?.content}} </p>
          <p>별점: {{review?.rating}} </p>
          <p>작성 시간: {{review?.created_at}} </p>
          <p>리뷰에 대한 좋아요 갯수: {{review?.like_users.length}} </p>
          <!-- 내 리뷰면 수정, 삭제 가능 -->
          <!-- 수정 버튼을 누르면 수정하는 폼을 띄워서 수정할 수 있게 만들기 -->
          <v-btn>수정</v-btn>
          <v-btn  @click="deleteReview">삭제</v-btn>
        </v-col>
</v-row>

<v-row>
<v-col v-if="comments">
  <p>댓글 갯수: {{comments?.length}}</p>
      <!-- 리뷰에 달린 댓굴들 -->
    <v-container 
    v-for="comment in comments"
    :key="comment.id">
    <p>작성자: {{comment.user}} -> 이거도 유저pk인데 유저 네임으로 바꿔야함 </p> 
    <p>내용: {{comment.content}}</p>
    <p>작성시간: {{comment.created_at}}</p>
    <!-- 만약에 내 이름이 작성자랑 같다면(유니크해서 ㄱㅊ), 수정/삭제버튼 표시하기 -->
    <!-- 개못생김 오른쪽에 이쁘게 만들어 -->
    <v-btn>수정</v-btn>
    <v-btn @click="deleteComment(comment.id)">삭제</v-btn>
        <ReplyForm 
        :comment="comment"
        @createReply="createReply"
        />
          
    </v-container>
</v-col>
      </v-row>
      <v-row>
  <v-col>
  <!-- 댓글 작성 -->
  <!-- 너무 커 작게 만들기 -->
  <v-card>
    <v-card-text>
      <v-textarea v-model="newComment" label="Your comment" 
      @keyup.enter="createComment" rows="1"
      />
      
    </v-card-text>
    <v-card-actions>
      <v-btn color="primary" @click.prevent="createComment">댓글 작성</v-btn>
    </v-card-actions>
  </v-card>
          <!-- 로그인 시 작성할 수 있게 -->
</v-col>
</v-row>
    </v-container>
</template>

<script>
import axios from 'axios'
import ReplyForm from '@/components/ReplyForm'

export default {
  components: {
    ReplyForm
  },
  data() {
    return {
      review: null,
      // comments: null,
      newComment: '',
      newreply: '',
    }
  },
  methods: {
    getReview() {
      const Token = this.myToken
      const reviewId = this.$route.params.reviewId
      // console.log(reviewId)
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/reviews/${reviewId}/`,
        headers: {
          Authorization: `Bearer ${Token}`
        },
      })
      .then((res) => {
        console.log(res.data)
        this.review = res.data
      })
      .catch((err) => console.log(err))
    },
    // 리뷰 삭제
    deleteReview() {
      const Token = this.myToken
      const reviewId = this.$route.params.reviewId
      
      axios({
        method: 'delete', 
        url: `http://127.0.0.1:8000/api/v1/reviews/${reviewId}/`,
        headers: {
          Authorization: `Bearer ${Token}`
        },
      })
      .then((res) => {
        console.log(res)
        alert('삭제되었습니다.')
        this.$router.go(-1)
      })
      .catch((e)=> console.log(e))
    },
    // 댓글 가져오기
    // getComment() {
    //   const Token = this.myToken
    //   const reviewId = this.$route.params.reviewId
    //   axios({
    //     method: 'get',
    //     url: `http://127.0.0.1:8000/api/v1/reviews/${reviewId}/comments/`,
    //     headers: {
    //       Authorization: `Bearer ${Token}`
    //     },
    //   })
    //   .then((res) => {
    //     console.log(res.data)
    //     // push 말고 맨 앞에 가져오거나 뭐 어케해야함
    //     this.comments = res.data
    //   })
    // },
    // 댓글 생성
    // 컴포넌트 나눠서 emit처리를 해야하나?
    createComment() {
      if (this.newComment === '') {
        // alert말고 뭐 어케든 하기
        alert('입력해')
      }
      else {
      const Token = this.myToken
      const reviewId = this.$route.params.reviewId
      const data = {
        content: this.newComment
      }
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/api/v1/reviews/${reviewId}/comments/`,
        headers: {
          Authorization: `Bearer ${Token}`
        },
        data
      })
      .then((res) => {
        console.log(res.data)
        this.newComment = ''
        this.getReview()
        // this.comments = res.data
      })
    }},
    deleteComment(commentId) {
      const Token = this.myToken
      
      axios({
        method: 'delete', 
        url: `http://127.0.0.1:8000/api/v1/comments/${commentId}/`,
        headers: {
          Authorization: `Bearer ${Token}`
        },
      })
      .then((res) => {
        console.log(res)
        alert('삭제되었습니다.')
        this.getReview()
      })
      .catch((e)=> console.log(e))
    },
    // 대댓글 작성
    createReply(childData) {
      const Token = this.myToken
      const reviewId = this.$route.params.reviewId
      const commentId = childData.commentId
      const data = {
        content: childData.newreply
      }
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/api/v1/reviews/${reviewId}/comments/${commentId}/replies/`,
        headers: {
          Authorization: `Bearer ${Token}`
        },
        data
      })
      .then((res) => {
        console.log(res)
        this.getReview()
      })
      .catch(e => console.log(e))
    }
  },
  created() {
    this.getReview()
    // this.getComment()
  },
  computed: {
    myToken() {
      return this.$store.state.account.accessToken
    },
    comments() {
      return this.review.comments
    }
  }
};
</script>
