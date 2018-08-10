import Vue from 'vue'
import Router from 'vue-router'
import index from '../components/index.vue'
import register from '../components/register.vue'
import login from '../components/login.vue'
import enroll from '../components/enroll.vue'
import admin from '../components/admin.vue'

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
      name:'register',
      component:register
    },
    {
      path:'/login',
      name:'login',
      component:login
    },
    {
      path:'/enroll',
      name:'enroll',
      component:enroll
    },
    {
      path:'/admin',
      name:'admin',
      component:admin
    }
  ]
})
