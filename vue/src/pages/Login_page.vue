
<template>
    <div>
        <login-status></login-status>
        <lo></lo>
    </div>
</template>

<script>
/* eslint-disable */
import login from '../components/Login.vue'
import loginStatus from '../components/Login_status.vue'
export default {
    name:'Login_page',
    components:{
        'lo':login,
        'login-status':loginStatus
    }
}


</script>

