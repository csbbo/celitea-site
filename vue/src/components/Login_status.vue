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
        var Login_status = false
        //get login status
        fetch(localhost.login_status,{
            method:"post"
        }).then(function(response){
            return response.json()
        }).then(function(json){
            Login_status = json.login_Status
            var get_userName = json.userName
        })
        return {
            isLogin:Login_status,
            userName:get_userName,
            url:"#/"
        }
    },
    methods:{
        user_Logout:function(){
            //send logout msg
            var post = {
                lgout:'true'
            }
            fetch(localhost.logout,{
                method:"post",
                body:post
            }).then(function(response){
                return response.json()
            }).then(function(json){
                if(json.logout === "ture"){
                    alert("Logout !")
                }
                else{
                    alert("Logout fail !")
                }
            })
        }
    }
}
</script>

