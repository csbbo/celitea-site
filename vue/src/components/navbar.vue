<template>
    <div>
    <b-navbar toggleable="md" type="dark" variant="info">
       <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
        <b-navbar-brand href="#/">Celitea</b-navbar-brand>
        <b-collapse is-nav id="nav_collapse">
            <b-navbar-nav>
                <b-nav-item  @click="enroll()">报名</b-nav-item>
                <b-nav-item href="#">关于我们</b-nav-item>
                <b-nav-item href="#">新手指导</b-nav-item>
            </b-navbar-nav>
            <b-navbar-nav class="ml-auto" >
                <b-nav-item-dropdown id="user_status" right>
                        <template slot="button-content">
                            <em>{{fi}}</em>
                        </template>
                    <b-dropdown-item @click="login()">{{ se }}</b-dropdown-item>
                    <b-dropdown-item @click="Signout()">{{ th }}</b-dropdown-item>
                </b-nav-item-dropdown>
            </b-navbar-nav>   
        </b-collapse>
        
    </b-navbar>
    </div>
</template>

<script>
import store from '../vuex/store.js'
import router from '../router/index.js'

export default {
    data(){
        store.commit('init_login_status')
        if(store.state.token === ''){
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
        },
        enroll()
        {
            if(store.state.token === ''){
                alert("请登陆之后再操作")
                this.$router.push('')  
            }
            else {
                this.$router.push('enroll')
                console.log("good enroll")
            }
        }
    },
    computed:{
        fi:function(){
            if(store.state.token === ''){
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


