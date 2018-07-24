
<template>
    <div>
        <login-status></login-status>
        <all-articles></all-articles>
    </div>
</template>

<script>
/* eslint-disable */
import allArticles from '../components/All_articles.vue'
import loginStatus from '../components/Login_status.vue'


export default {
    name:'index',
    components:{
        'all-articles':allArticles,
        'login-status':loginStatus
    }
}




</script>
