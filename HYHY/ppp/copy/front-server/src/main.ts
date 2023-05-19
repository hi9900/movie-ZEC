import { createApp } from 'vue'
import { createPinia } from 'pinia'
import VueTippy from 'vue-tippy'
import App from './App.vue'

const app = createApp(App)
app.use(createPinia())
app.use(VueTippy, {
	theme: 'standard-dark',
	defaultProps: { 
		placement: 'right',
		delay: [0, 0],
		duration: 0,
		allowHTML: true,
		maxWidth: 150,
		theme: 'standard-dark'
	},
})

app.mount('#app')