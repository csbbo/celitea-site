<template>
  <div id="register-div">
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <b-form-group id="exampleInputGroup1"
                    label="You Phone Number:"
                    label-for="exampleInput1"
                    description="We'll never share your number with anyone else.">
        <b-form-input id="exampleInput1"
                      type="tel"
                      v-model="form.userPhoneNumber"
                      required
                      placeholder="Enter phonenumber">
        </b-form-input>
        </b-form-group>
        <b-form-group id="exampleInputGroup2"
                    label="Your Name:"
                    label-for="exampleInput2">
        <b-form-input id="exampleInput2"
                      type="text"
                      v-model="form.userName"
                      required
                      placeholder="Enter name">
        </b-form-input>
        </b-form-group>
        <b-form-group label="Your password"
                    label-for="exampleInput2">
        <b-form-input type="password"
                    v-model="form.userPassword"
                    required
                    placeholder="Enter password">
        </b-form-input>
        </b-form-group>
        <b-form-group label="Identifying code">
            <b-form-input type="text"
                         v-model="form.userIdentifyingCode"
                         required
                        placeholder="Enter code">
            </b-form-input>
            <b-button type="getIdentifyCode">Get</b-button>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </div>
</template>

<script>
import router from '../router/index.js'

export default {
  data () {
    return {
      form: {
        userPhoneNumber: '',
        userName: '',
        userPassword:'',
        userIdentifyingCode:''
      },
      show: true
    }
  },
  methods: {
    onSubmit (evt) {
        evt.preventDefault();
        var data_jsnop = 'userPhoneNumber'+'='+this.form.userPhoneNumber+'&'+'userName'+'='+this.form.userName+'&'+'userPassword'+'='+this.form.userPassword+'&'+'userIdentifyingCode'+'='+this.form.userIdentifyingCode
        console.log(data_jsnop);
        fetch('http://ccssbb.cn/regist//',{
            method:'POST',
            headers:{
              "Content-Type": "application/x-www-form-urlencoded"
            },
            body:data_jsnop,
            mode: 'cors',
            cache: 'no-cache',
            credentials:'include',
        }).then(function(response){
          return response.json()
        }).then(function(json){
          console.log(json);
          if(json.registerStatus === "wrongCode")
            alert("Wrong Code");
          else if(json.registerStatus === "fail")
            alert("Register fail!")
          else{
            alert("Register success !")
            router.push('login')
          }
        })
    },
    onReset (evt) {
      evt.preventDefault();
      /* Reset our form values */
      this.form.userPhoneNumber = '';
      this.form.userName = '';
      this.form.userPassword = '';
      this.form.userIdentifyingCode = '';
      /* Trick to reset/clear native browser form validation state */
      this.show = false;
      this.$nextTick(() => { this.show = true });
    }
  }
}
</script>


<style>
    #register-div{
        width: 60%;
        float: left;
        margin: 0 10%;
    }
</style>
