<template>
    <div>
        <div v-if="!isLogin">
            <a href="#/login"><p>Login</p></a>
            <a href="#/register"><p>Register</p></a>
        </div>
        <div v-if="isLogin">
        <p>Hi! {{userName}} </p>
        <a href="#/" @click="user_Logout">Logout</a>
        </div>
    </div>
</template>

<script>
/* eslint-disable */
export default {
    data:function(){
        var Login_status = true
        //get login status
        if(Login_status){
            //get userName
            var get_userName = "Test"
        }
        return {
            isLogin:Login_status,
            userName:get_userName
        }
    },
    methods:{
        user_Logout:function(){
            //send logout msg
            alert("Logout!")
        }
    }
}
</script>

