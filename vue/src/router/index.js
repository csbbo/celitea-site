import Vue from 'vue'
import VueRouter from '../../node_modules/vue-router';
import index from '../components/index.vue'
import register from '../components/register.vue'
import login from '../components/login.vue'
import enroll from '../components/enroll.vue'
import admin from '../components/admin.vue'
import article from '../components/article.vue'

Vue.use(VueRouter)
const routes =  [
  {
    path: '/',
    name: 'index',
    component: index,
  },
  {
    path:'/:id',
    name:'article',
    component:article
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

const router  = new VueRouter({
  routes:routes
})

export default router

