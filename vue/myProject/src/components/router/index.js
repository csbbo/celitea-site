/* eslint-disable */

import Vue from 'vue'
import Router from 'vue-router'
import index from '../pages/index.vue'
import Login_page from '../pages/Login_page.vue'
import Register_page from '../pages/Register_page.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path:'/register',
      name:'Register',
      component:Register_page
    },
    {
      path:'/login',
      name:'Login',
      component:Login_page
    }
  ]
})
