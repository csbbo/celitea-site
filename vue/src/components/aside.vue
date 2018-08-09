<template>
    <div id="aside-div">
       <b-nav vertical class="w-25" pills>
            <b-nav-item router-tag="#/" @click="enroll()" >报名</b-nav-item>
            <b-nav-item  router-tag="#/" >关于我们</b-nav-item>
            <b-nav-item router-tag="#/" >新手指导</b-nav-item>
        </b-nav>
    </div>
</template>

<script>
import store from '../vuex/store.js'
export default {
    methods:{
        enroll()
        {
            
            if(store.state.token === ''){
                alert("请登陆之后再操作")
                this.$router.push('')  
            }
            else {
                this.$router.push('enroll')
                console.log("good enroll")
            }
        }
    }
}
</script>


<style>
    #aside-div{
        width: 20%;
        float: left;
    }
</style>

