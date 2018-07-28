<template>
    <div>
       <el-form ref="form" :model="form" label-position="left" label-width="10%"  >
           <el-form-item label="UserPhone">
               <el-input v-model="form.userphone"  style=" width:40% " ></el-input>
           </el-form-item>
           <el-form-item label="UserPassword">
               <el-input v-model="form.userpassword" style=" width:40% " ></el-input>
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
                userphone:'', 
                userpassword:'',
            }
        }
    },
    methods:{
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


<style>
    .el-form{
        width: 80%;
        margin: 10px auto;
    }
    .el-form-item{
        width: 100%;
        margin: 20px auto;
    }
</style>

