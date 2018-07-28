
<template>
    <div>
        <form v-on:submit="submit_infom()" name="Login">
        <label>userPhone</label><input type="tel" name="userPhone"/>
        <label>userPassword</label><input type="password" name="userPassword"/>
        <a v-bind:href="url"><input type="submit"/></a>
        </form>
    </div>
</template>

<script>
/* eslint-disable */
export default {
    data:function(){
        return {
            url:'#/'
        }
    },
    methods:{
        submit_infom:function(){
            var post = {
                user:{
                    userName:Login.userPhone.value,
                    userPassword:Login.userPassword.value
                }
            }
            fetch('http://ccssbb.cn/login',{
                method:"post",
                body:post
            }).then(function(response){
                return response.json()
            }).then(function(json){
                if(json.lofinStatus === "success"){
                    alert("login success!")
                    this.url = "#/"
                }
                else{
                    alert("login fail")
                    this.url = "#/login"
                }   
            })
        }

    }
}
</script>
