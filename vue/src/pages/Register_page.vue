
<template>
    <div>
        <login-status></login-status>
        <re></re>
    </div>

</template>

<script>
/* eslint-disable */
import Re from '../components/Register.vue'
import loginStatus from '../components/Login_status.vue'

export default {
    name:'Register_page',
    components:{
        're':Re,
        'login-status':loginStatus
    }
}


</script>

