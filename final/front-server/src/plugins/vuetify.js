import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import "vuetify/dist/vuetify.min.css";

Vue.use(Vuetify);

const getDarkTheme = () => {
  const theme = localStorage.getItem("darkTheme");
  return theme === "true";
};

export default new Vuetify({
  theme: {
    dark: getDarkTheme(),
    themes: {
      light: {
        primaryBackground: "#ffffff",
        maxBackground: "#ffffff", // 1260px 이하에서 사용할 배경색
      },
      dark: {
        primaryBackground: "#1a1a1a",
        maxBackground: "#1a1a1a", // 1260px 이하에서 사용할 배경색
      },
    },
  },
});