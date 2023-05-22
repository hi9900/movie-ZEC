import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import "vuetify/dist/vuetify.min.css";

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    dark: true,
    // themes: {
    //   dark: {
    //     appBarColor: '#14181C',
    //     footerColor: '#2C3440',
    //     background: '#14181d',
    //   }
    // }
  },
});