<template>
    <div class="self-com">
        <b-tabs>
            <b-tab title="查看报名信息">
                <br>
                <b-table striped hover :items="items"></b-table>
            </b-tab>
            <b-tab title="添加文章">
                <br>
                <div ref="editor" style="text-align:left"></div>
                <b-button @click="submit">提交</b-button>
            </b-tab>
            <b-tab title="修改文章">
                <br>
                <div>222</div>
            </b-tab>
        </b-tabs>
    </div>
</template>


<script>
import E from 'wangeditor'
import store from '../vuex/store';

const items = [
  { isActive: true, age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
  { isActive: false, age: 21, first_name: 'Larsen', last_name: 'Shaw' },
  { isActive: false, age: 89, first_name: 'Geneva', last_name: 'Wilson' },
  { isActive: true, age: 38, first_name: 'Jami', last_name: 'Carney' }
]

export default {
    data(){
        return {
            editorContent:'',
            items:items
        }
    },
    mounted(){
        var editor = new E(this.$refs.editor)
        editor.customConfig.onchange = (html) =>{
            this.editorContent = html
        }
        editor.create()
    },
    methods:{
        submit(){
            fetch('http://ccssbb.cn/articles/',{
                headers:{
                    "Authorization":store.state.token
                },
                method:"post",
                body:this.editorContent
            }).then(function(response){
                return response.json()
            }).then(function(json){
                if(json.loginStatu === 'fail')
                    alert("登陆失效")
                else if(json.add_article === 'success')
                    alert("添加成功")
                else {
                    alert("添加失败")
                }
            })
        }
    }
    
    
}
</script>





