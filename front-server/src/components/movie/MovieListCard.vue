<template>
  <!-- 이 페이지 로딩화면 구현해야함 -->
  <v-container fluid>
    <v-card
      @mouseover="isHover = true"
      @mouseleave="isHover = false"
      :class="['card-container', cardHeightClass, {'hover-card': isHover}]"
      class="fixed-height grow-on-hover your-card"
    >
      <!-- <v-card class="card-container fixed-height grow-on-hover" height="100%"> -->
      <div class="movieCard" @click="goToDetail(movie.id)">
        <div class="pa-2 pb-0">
          <v-img
            relative
            hight="200px"
            aspect-ratio="0.675"
            :src="
              'https://image.tmdb.org/t/p/w600_and_h900_bestv2' +
              movie.poster_path
            "
          >
            <!-- 작을때 -->
            <div
              class="d-none d-lg-none text-overlay absolute d-flex flex-column align-center"
              v-if="isHover"
              style="
                width: 100%;
                height: 100%;
                background-color: rgba(0, 0, 0, 0.7);
                color: white;
                justify-content: flex-start;
                padding-top: 45%;
              "
            >
              <h3
                class="ellipsis-second-line"
                style="font-size: 1.5em; text-align: center"
              >
                {{ movie.title }}
              </h3>
              <p
                class="text--disabled original_title"
                style="font-size: 1.2em; text-align: center"
              >
                {{ movie.original_title }}
              </p>
            </div>
          </v-img>
        </div>
        <v-card-title primary-title class="d-md-block d-none">
          <div class="body-1 ellipsis-second-line">{{ movie.title }}</div>
          <p class="caption text--disabled original_title">
            {{ movie.original_title }}
          </p>
        </v-card-title>
      </div>
      <!-- <v-card-actions
        class="card-actions fixed-bottom d-md-block d-none"
        :class="cardActionsClass"
      >
        <v-row no-gutters align="center" justify="center" class="card-actions">
          <v-col cols="4" class="text-center">
            <v-icon :color="WatchIconColor ? 'blue' : ''">mdi-eye</v-icon>
          </v-col>
          <v-col cols="4" class="text-center">
            <v-icon :color="heartIconColor ? 'red' : ''">mdi-heart</v-icon>
          </v-col>

          <v-col cols="4" class="text-center">
            <v-tooltip top>
              <template v-slot:activator="{on, attrs}">
                <v-icon
                  v-bind="attrs"
                  v-on="on"
                  :color="starIconColor ? 'yellow' : ''"
                >
                  mdi-star
                </v-icon>
              </template>
              <span>Tooltip text</span>
            </v-tooltip>
          </v-col>
        </v-row>
      </v-card-actions> -->
    </v-card>
  </v-container>
</template>

<script>
export default {
  props: {
    movie: Object
  },
  data() {
    return {
      // WatchIconColor: false,
      // heartIconColor: false,
      // starIconColor: false,
      isHover: false,
      isMaxWidth: window.innerWidth <= 1260
    }
  },
  methods: {
    goToDetail(movieId) {
      this.$router.push({name: 'MovieDetail', params: {id: movieId}})
    },
    onResize() {
      this.isMaxWidth = window.innerWidth <= 1260
    }
  },
  computed: {
    WatchIconColor() {
      const review = this.$store.getters[('profile/userReviews', this.movie.id)]
      return review ? review.watched : false
    },
    heartIconColor() {
      const review = this.$store.getters[('profile/userReviews', this.movie.id)]
      return review ? review.liked : false
    },
    starIconColor() {
      const review = this.$store.getters[('profile/userReviews', this.movie.id)]
      return review ? review.rating >= 3 : false
    },
    cardHeightClass() {
      if (this.$vuetify.breakpoint.smAndDown) {
        return 'small-card-height'
      } else if (this.$vuetify.breakpoint.lg) {
        return 'large-card-height'
      } else if (this.$vuetify.breakpoint.md) {
        return 'middle-card-height'
      } else {
        return 'default-card-height'
      }
    },
    cardActionsClass() {
      if (this.isMaxWidth) {
        const theme = this.$vuetify.theme.dark ? 'dark' : 'light'
        console.log(theme)
        return `card-actions-max-${theme}`
      }
      return ''
    }
  },
  mounted() {
    this.$nextTick(function () {
      window.addEventListener('resize', this.onResize)
    })
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.onResize)
  }
}
</script>

<style scoped>
.fixed-height {
  height: 400px;
  min-height: 400px;
  max-height: 400px;
  overflow: hidden;
}
.ellipsis-second-line {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  overflow: ellipsis;
  text-overflow: ellipsis;
  width: 100%;
  word-wrap: break-word;
  word-break: keep-all;
}
.movieCard {
  cursor: pointer;
}
.card-container {
  position: relative;
}
.fixed-bottom {
  position: absolute;
  bottom: 0;
  width: 100%;
}
.original_title {
  word-break: keep-all;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  overflow: hidden;
  overflow: ellipsis;
  text-overflow: ellipsis;
}
.grow-on-hover {
  transition: transform 0.3s ease-in-out;
}
.grow-on-hover:hover {
  transform: scale(1.05);
}

.small-card-height {
  height: 250px;
  min-height: 250px;
  max-height: 250px;
}
.large-card-height {
  height: 370px;
  min-height: 370px;
  max-height: 370px;
}
.middle-card-height {
  height: 320px;
  min-height: 320px;
  max-height: 320px;
}
.default-card-height {
  height: 400px;
  min-height: 400px;
  max-height: 400px;
}

.card-actions {
  background-color: transparent !important;
}
/* @media (max-width: 1260px) {
  .card-actions {
    background-color: #1a1a1a;
  }
}  */
</style>
