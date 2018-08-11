<template>
    <div class="self-com">
        <b-tabs>
            <b-tab title="查看报名信息">
                <br>
                <b-table striped responsive hover 
                :busy.sync="isBusy"
                :fields="fields" 
                :items="get_items"> 
                    <span  slot="头像"  slot-scope="data" v-html="data.item.avatar_url"></span>
                    <template slot="姓名" slot-scope="data">
                        {{data.item.name}}
                    </template>
                    <template slot="学号" slot-scope="data">
                        {{data.item.stu_num}}
                    </template>
                    <template slot="介绍" slot-scope="data">
                        {{data.item.introduction}}
                    </template>
                    <template slot="邮箱" slot-scope="data">
                        {{data.item.email}}
                    </template>
                    <template slot="电话号码" slot-scope="data">
                        {{data.item.phone}}
                    </template>
                    <template slot="心中的Celitea" slot-scope="data">
                        {{data.item.think_celitea}}
                    </template>
                    <template slot="希望学到什么" slot-scope="data">
                        {{data.item.want_learn}}
                    </template>
                    <template slot="'技能成果" slot-scope="data">
                        {{data.item.skill}}
                    </template>
                    <template slot="用户ID" slot-scope="data">
                        {{data.item.user_id}}
                    </template>
                </b-table>
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


export default {
    data(){
            return {
                isBusy:false,
                editorContent:'',
                fields:[
                '头像',
                '姓名',
                '学号',
                '介绍',
                '技能成果',
                '希望学到什么',
                '心中的Celitea',
                '邮箱',
                '电话号码',
                '用户ID', 
                ]
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
        ,
        get_items(ctx){
            let promise = fetch('http://ccssbb.cn/applylist/',{
                headers:{
                    "Authorization":store.state.token
                },
                method:'get',
            })
            return promise.then(function(response){
                return response.json().then(function(json){
                    console.log(json)
                    console.log('1')
                        if(json.loginStatu === "fail"){
                        alert("登陆失效")
                        return []
                    }   
                    else if(json.isadmin === "no"){
                        alert("not admin")
                        return []
                    } 
                    else{
                        for(var i in json){
                            console.log(json)
                            console.log(json[i])
                            json[i].avatar_url = '<img src="' + json[i].avatar_url +'" />'
                            console.log(json[i].avatar_url)
                        }
                        return json
                    }
                })
                
            }
            )             
        }
    }
}
</script>





