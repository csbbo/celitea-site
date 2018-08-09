<template>

    <div id="enroll-div">
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
                    v-model="form.avatar"
                    placeholder="Choose a file...">
                </b-form-file>
            </b-form-group>

            <b-button type="submit" variant="primary">提交</b-button>
        </b-form>
    </div>
</template>


<script>
import store from '../vuex/store';

export default {
    data (){
        return {
            form:{
                name:'',
                stu_num:'',
                phone:'',
                eamil:'',
                introduction:'',
                skill:'',
                want_learn:'',
                think_celitea:'',
                avatar:''
            }
        }
    },
    methods:{
        submit()
        {
            console.log(this.form)
            fetch('http://ccssbb.cn',{
                headers:{
                    'content-type':'application/json',
                    'Authorization':store.state.token
                },
                body:JSON.stringify(this.form)
            }).then(function(response){
                return response.json()
            }).then(function(json){
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
</script>

<style>
    #enroll-div{
        width: 60%;
        float: left;
        margin: 0 10%;
    }
</style>

