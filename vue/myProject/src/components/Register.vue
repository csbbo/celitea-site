
<template>
    <div>
        <form v-on:submit="submit_infom()" name="register">
        <label>userName</label><input type="text" name="userName"/>
        <label>userPassword</label><input type="password" name="userPassword"/>
        <label>userPhone</label><input type="tel" name="userPhone"/><button  @click="get_identifying_code()" type="button" > 获取验证码</button>
        <label>identifyingCode</label><input type="text" /><br>
        <input type="submit"/>
        </form>
    </div>
</template>

<script>
/* eslint-disable */
export default {
    methods:{
        get_identifying_code:function(){
            //
            console.log("hello")
        },
        submit_infom:function(){
            console.log("test")
            console.log({
                userName:register.userName.value,
                userPassword:register.userPassword.value,
                userPhone:register.userPhone.value
            })
            alert()
        }

    }
}
</script>
