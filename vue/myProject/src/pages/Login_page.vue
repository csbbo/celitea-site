
<template>
    <div>
        <login-statue></login-statue>
        <lo></lo>
    </div>
</template>

<script>
/* eslint-disable */
import login from '../components/Login.vue'
import loginStatue from '../components/Login_statue.vue'
export default {
    name:'Login_page',
    components:{
        'lo':login,
        'login-statue':loginStatue
    }
}


</script>

