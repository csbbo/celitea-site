<template>
    <div class="self-com">
        <b-card  v-for="item in items" :key="item.id"  :title="item.article_title"  :sub-title="item.time">
        <p class="card-text">
            {{item.article}}    
        </p>
        <a href="#" class="card-link">Card link</a>
        <b-link href="#" class="card-link">Another link</b-link>
    </b-card>
    </div>
</template>


<script>
export default {
    computed:{
        items:function(){
            // let promise = fetch('http://ccssbb.cn/',{
            //     method:'get'
            // })
            // return promise.then(function(response){
            //     return response.json()
            // })
            return [
                {
                    'article':'article',
                    'article_title':'article_title',
                    'id':'1',
                    'time':'1'
                },
                {
                    'article':'article',
                    'article_title':'article_title',
                    'id':'2',
                    'time':'2'
                },
                {
                    'article':'article',
                    'article_title':'article_title',
                    'id':'3',
                    'time':'3'
                }
            ]
        }
    }
}
</script>



