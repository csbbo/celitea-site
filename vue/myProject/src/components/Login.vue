
<template>
    <div>
        <form v-on:submit="submit_infom()" name="Login">
        <label>userPhone</label><input type="tel" name="userPhone"/>
        <label>userPassword</label><input type="password" name="userPassword"/>
        <input type="submit"/>
        </form>
    </div>
</template>

<script>
/* eslint-disable */
export default {
    methods:{
        submit_infom:function(){
                console.log({
                userName:Login.userPhone.value,
                userPassword:Login.userPassword.value
            }),
            alert("good")
        }

    }
}
</script>
