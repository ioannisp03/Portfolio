import './assets/main.css'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap-icons/font/bootstrap-icons.css";
import "toastify-js/src/toastify.css"; 
import "bootstrap"


import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// import '@/assets/js/main.js'


const app = createApp(App)

app.use(router)

app.mount('#app')
