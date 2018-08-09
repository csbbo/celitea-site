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
        <b-form-group label="Your password"
                    label-for="exampleInput2">
        <b-form-input type="password"
                    v-model="form.userPassword"
                    required
                    placeholder="Enter password">
        </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </div>
</template>

<script>

import router from '../router/index.js'
import store from '../vuex/store.js'

export default {
  data () {
    return {
      form: {
        userPhoneNumber: '',
        userPassword:'',
      },
      show: true
    }
  },
  methods: {
    onSubmit (evt) {
      evt.preventDefault();
      var data_jsnop = 'userPhoneNumber' +'='+this.form.userPhoneNumber+'&'+'userPassword'+'='+this.form.userPassword
      console.log(data_jsnop)
      fetch('http://ccssbb.cn/login/',{
          method:'POST',
          headers:{
            "Content-Type": "application/x-www-form-urlencoded"
          },
          body:data_jsnop,
          credentials:'include',
      }).then(function(response){
          return response.json()
      }).then(function(json){
        if(json.loginStatus === "true"){
          console.log(json.token)
          store.commit('note_login_status',json.userName,json.token)
          alert("Login Success !")
          router.push('/')
        }
        else
          alert("login fail!")

      })
    },
    onReset (evt) {
      evt.preventDefault();
      /* Reset our form values */
      this.form.userPhoneNumber = '';
      this.form.userPassword = '';
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
