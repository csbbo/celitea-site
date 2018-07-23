
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
            console.log("good")
            return {
                posts:[
                    {id:'1',title:'one',content:'1111111'},
                    {id:'2',title:'two',content:'2222222'},
                    {id:'3',title:'three',content:'3333333'},
                    {id:'4',title:'four',content:'4444444'},
                    {id:'5',title:'five',content:'5555555'}
                ]
            }
        }
    }
</script>
