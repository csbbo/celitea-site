
<template>
    <div>
    <div v-for="post in posts" v-bind:key="post.id">
        <h4> {{post.title}} </h4>
        <p> {{post.content}} </p>
    </div>
    </div>
</template>

<script>
/* eslint-disable */
    export default{
        data:function(){
             //get data
            fetch(ccssbb.cn/index,{
                method:"get"
            }).then(function(response){
                return response.json()
            }).then(function(json){
                var posts = json.posts
            })
           //---------------
            console.log("posts")
            //-----------------
            return posts
        }
    }
</script>
