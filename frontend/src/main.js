import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.prototype.axios = axios
Vue.config.productionTip = false
Vue.use(ElementUI)


new Vue({
  render: h => h(App),
  el: '#app',
  router,
  components: {
    App
  },
  template: '<App/>'
})