<template>
    <div>
    <b-navbar toggleable="md" type="dark" variant="info">
      <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
      <b-navbar-brand href="#/">NavBar</b-navbar-brand>
        <b-collapse is-nav id="nav-collapse">
        </b-collapse>
        <b-nav-item-dropdown id="user_status" right>
            <template slot="button-content">
                <em>{{fi}}</em>
            </template>
          <b-dropdown-item @click="login()">{{ se }}</b-dropdown-item>
          <b-dropdown-item @click="Signout()">{{ th }}</b-dropdown-item>
        </b-nav-item-dropdown>
    </b-navbar>
    </div>
</template>

<script>
import store from '../vuex/store.js'
import router from '../router/index.js'

export default {
    data(){
        if(store.state.userName === ''){
            return {
                se:"login",
                th:"register",
            }
        }
        else{
            return {
                se:"Main",
                th:"Signout",
            }
        }
    },
    methods:{
        login()
        {
            if(store.state.token === '')
                router.push('login')
            else{
                router.push('/')
            }
        },
        Signout()
        {
            if(store.state.token === '')
                router.push('register')
            else{
                store.commit('clear_login_status')
                router.push('/') 
            }
        }
    },
    computed:{
        fi:function(){
            if(store.state.userName === ''){
                this.se = "login",
                this.th = "register"
                return "Please login"
            }    
            else {
                this.se = "Main",
                this.th = "Signout"
                return store.state.userName
            }   
                
        }
    }
}
</script>


<style>

    #user_status{
        list-style: none;
        text-align: center;
    }

    #user_status em{
        color: aliceblue;
    }
</style>


