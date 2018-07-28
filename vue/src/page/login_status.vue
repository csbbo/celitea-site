<template>
    <div>
        <el-menu :default-active="activeIndex" mode="horizontal"   router="true"> 
            <el-menu-item index="/"><img src="../assets/logo.png" height="60px"/></el-menu-item>
            <el-menu-item :index="url1">{{ loginStatus }}</el-menu-item>
            <el-menu-item :index="url2" >{{Register}}</el-menu-item>
        </el-menu>
    </div>
</template>

<script>
export default {
    data(){
        var islogin = false
        var login = ''
        //get login status
        if(islogin){
            return {
                islogin:'true',
                loginStatus: 'Hi!'+ login,
                url1:'/',
                Register:'Logout',
                url2:'/',
            }
        }
        else{
            return {
                islogin:'false',
                loginStatus:'Login',
                url1:'/login',
                Register:'Register',
                url2:'/register'
            }
        }
    }
}
</script>

<style>
    .el-menu{
        width: 100%;
        float: left;
    }
</style>

