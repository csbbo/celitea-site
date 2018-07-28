<template>
    <div>
       <el-form ref="form" :model="form" label-position="left" label-width="13%"  >
           <el-form-item label="UserName">
               <el-input v-model="form.username"  style=" width:40% " ></el-input>
           </el-form-item>
           <el-form-item label="UserPassword">
               <el-input v-model="form.userpassword" style=" width:40% " ></el-input>
           </el-form-item>
           <el-form-item label="UserPhone" :inline="true">
               <el-input v-model="form.userphone" style=" width:40% " ></el-input>
               <el-button @click="getIdentifyingCode" style=" width:20%" >GetCode</el-button>
           </el-form-item>
            <el-form-item label="IdentifyingCode">
               <el-input v-model="form.identifyingcode" style=" width:40% " ></el-input>
           </el-form-item>
            <el-form-item >
                <el-button @click="onSubmit" style=" width:20%" >put</el-button>
            </el-form-item>
       </el-form>
    </div>
</template>

<script>
export default {
    data(){
        return {
            form:{
                username:'',
                userpassword:'',
                userphone:'',
                identifyingcode:''
            }
        }
    },
    methods:{
        getIdentifyingCode(){
            
        },
        onSubmit(){
            console.log(JSON.stringify(this.form))
            fetch('http://ccssbb.cn/regist',{
                method:"post",
                body:JSON.stringify(this.form) 
            }).then(function(response){
                console.log(JSON.stringify(this.form))
                return response.json()
            }).then(function(json){
                console.log(json)
            })
        }
    }
}
</script>



