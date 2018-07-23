
<template>
    <div>
        <login-statue></login-statue>
        <re></re>
    </div>

</template>

<script>
/* eslint-disable */
import Re from '../components/Register.vue'
import loginStatue from '../components/Login_statue.vue'

export default {
    name:'Register_page',
    components:{
        're':Re,
        'login-statue':loginStatue
    }
}


</script>

