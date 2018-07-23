
<template>
    <div>
        <login-statue></login-statue>
        <all-articles></all-articles>
    </div>
</template>

<script>
/* eslint-disable */
import allArticles from '../components/All_articles.vue'
import loginStatue from '../components/Login_statue.vue'


export default {
    name:'index',
    components:{
        'all-articles':allArticles,
        'login-statue':loginStatue
    }
}




</script>
