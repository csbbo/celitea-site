<template>

    <div class="self-com">
        <b-form @submit="submit">
            <b-form-group horizontal
                breakpoint="lg"
                label="基本信息"
                label-size="lg">

            <b-form-group 
                id="InputGroup1"
                label="姓名"
                label-for="Input1">
                <b-form-input
                    id="Input1"
                    type="text"
                    v-model="form.name"
                    required>
                </b-form-input>
            </b-form-group>

            <b-form-group 
                id="InputGroup2"
                label="学号"
                label-for="Input2">
                <b-form-input
                    id="Input2"
                    type="text"
                    v-model="form.stu_num"
                    required>
                </b-form-input>
            </b-form-group>

            </b-form-group>
            <b-form-group horizontal
                breakpoint="lg"
                label="联系方式"
                label-size="lg">

                <b-form-group
                    id="InputGroup3"
                    label="电话号码"
                    label-for="Input3">
                    <b-form-input
                        id="input3"
                        type="tel"
                        v-model="form.phone"
                        required>
                    </b-form-input>
                </b-form-group>

                <b-form-group
                    id="InputGroup4"
                    label="邮箱"
                    label-for="Input4">
                    <b-form-input
                        id="input4"
                        type="email"
                        v-model="form.email"
                        required>
                    </b-form-input>
                </b-form-group>
            </b-form-group>

            <b-form-group
                id="InputGroup5"
                label="个人简介："
                label-for="Input5">
                <b-form-textarea
                    id="Input5"
                    v-model="form.introduction"
                    :rows="3"
                    :max-rows="5">
                </b-form-textarea>
            </b-form-group>

            <b-form-group
                id="InputGroup6"
                label="计算机方面技能与成果："
                label-for="Input6">
                <b-form-textarea
                    id="Input6"
                    v-model="form.skill"
                    :rows="3"
                    :max-rows="5">
                </b-form-textarea>
            </b-form-group>

            <b-form-group
                id="InputGroup7"
                label="你心中的计算机精英协会："
                label-for="Input7">
                <b-form-textarea
                    id="Input7"
                    v-model="form.think_celitea"
                    :rows="3"
                    :max-rows="5">
                </b-form-textarea>
            </b-form-group>

            <b-form-group
                id="InputGroup8"
                label="你希望能从我们社团学到什么"
                label-for="Input8">
                <b-form-textarea
                    id="Input8"
                    v-model="form.want_learn"
                    :rows="3"
                    :max-rows="5">
                </b-form-textarea>
            </b-form-group>

            <b-form-group
                id="InputGroup9"
                label="上传头像"
                label-for="Input9">
                <b-form-file
                    id="Input9"
                    accept="image/*"
                    v-model="file"
                    placeholder="Choose a file...">
                </b-form-file>
            </b-form-group>

            <b-button type="submit" variant="primary">提交</b-button>
        </b-form>
    </div>
</template>


<script>
import store from '../vuex/store';
import router from '../router/index.js'


export default {
    data (){
        return {
            form:{
                name:'',
                stu_num:'',
                phone:'',
                email:'',
                introduction:'',
                skill:'',
                want_learn:'',
                think_celitea:'',
                avatar:''
            },
            file:''
        }
    },
    methods:{
        submit()
        {
            var file = new FileReader()
            file.readAsDataURL(this.file)
            var temp = this.form
            file.onload = function(){
                console.log(temp)
                temp.avatar = file.result
                var data_jsonp = "name"+"="+ temp.name +"&"+"stu_num"+"="+ temp.stu_num+"&"+"phone"+"="+temp.phone+"&"+"email"+"="+temp.email+"&"+"introduction"+"="+temp.introduction+"&"+"skill"+"="+temp.skill+"&"+"want_learn"+"="+temp.want_learn+"&"+"think_celitea"+"="+temp.think_celitea+"&"+"avatar"+"="+file.result
                console.log(JSON.stringify(temp))
                fetch('http://ccssbb.cn/applications//',{
                    headers:{
                        'content-type':'application/x-www-form-urlencoded',
                        // 'content-type':"application/json",
                        'Authorization':store.state.token
                    },
                    body:data_jsonp,
                    // body: JSON.stringify(temp),
                    method:"post"
                }).then(function(response){
                return response.json()
                }).then(function(json){
                    console.log(json)
                    if(json.loginStatu === 'fail'){
                       alert("登陆失效，请重新登陆!")
                       router.push('login')
                   }
                    else if(json.apply === 'success'){
                        alert("报名成功！")
                        router.push('/')
                    }
                    else{
                        alert("报名失败！")
                    }
                })
            }
        }
    }
}
</script>











