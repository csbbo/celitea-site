
<template>
    <div>
        <form v-on:submit="submit_infom()" name="register">
        <label>userName</label><input type="text" name="userName"/>
        <label>userPassword</label><input type="password" name="userPassword"/>
        <label>userPhone</label><input type="tel" name="userPhone"/><button  @click="get_identifying_code()" type="button" > 获取验证码</button>
        <label>identifyingCode</label><input type="text" name="userIdentifyingCode" /><br>
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
        get_identifying_code:function(){
            //
            console.log("hello")
        },
        submit_infom:function(){
             var post = {
                user:{
                    userName:register.userName.value,
                    userPassword:register.userPassword.value,
                    userPhone:register.userPhone.value,
                    userIdentifyingCode:register.userIdentifyingCode.value
                }
            };
            fetch(ccssbb.cn/regist,{
                method:"post",
                body:post
            }).then(function(response){
                return response.json()
            }).then(function(json){
                //-----------
                console.log(json)
                //-----------------
                if(json.registerStatus === "fail"){
                    alert("Register fail !")
                    this.url = "#/register"
                }
                else if(json.registerStatus === "wrongCode"){
                    alert("wrong code !")
                    this.url = "#/register"
                }
                else alert("register success !")
            })
        }

    }
}
</script>
