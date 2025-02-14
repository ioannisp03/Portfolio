import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-icons/font/bootstrap-icons.css';
import './assets/main.css';
import * as bootstrap from "bootstrap";
import i18n from './i18n';

window.bootstrap = bootstrap;

import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

const app = createApp(App);
app.use(i18n)
app.use(router);
app.mount("#app");

import 'bootstrap/dist/js/bootstrap.bundle.min.js';

