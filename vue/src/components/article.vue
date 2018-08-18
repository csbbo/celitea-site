<template>
    <b-card>
        <b-media>
        <h3 class="mt-0">{{items.article_title}}</h3>
        <small>{{items.time}}</small>
        <div v-html="items.article"></div>
        </b-media>
    </b-card>
</template>

<script>
import store from '../vuex/store.js'


export default {
        
            data(){

                var items = {
                    article:'',
                    article_title:'',
                    time:''
                }
                console.log('1')
                var id = this.$route.params.id
                fetch('http://ccssbb.cn/apply_article/',{
                    headers:{
                        'Authorization':store.state.token,
                        'content-type':'application/x-www-form-urlencoded',
                    },
                    body:'aritcle_id'+'='+id,
                    method:'post'
                }).then(function(response){
                    return response.json()
                }).then(function(json){
                    items.article = json.article
                    items.article_title = json.article_title
                    items.time = json.items
                    console.log('2')
                })
                console.log('3')
                return {
                    items
                }
            }
        

}
</script>

