import { createApp } from 'vue'
import App from './App.vue'
import router from "./router/router";
import store from "./store/index";

const Vue = createApp(App);

Vue.use(store);
Vue.use(router);

Vue.mount('#app');