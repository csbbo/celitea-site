<template>
  <div class="self-com">
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <b-form-group id="exampleInputGroup1"
                    label="电话号码:"
                    label-for="exampleInput1">
        <b-form-input id="exampleInput1"
                      type="tel"
                      v-model="form.userPhoneNumber"
                      required
                      placeholder="Enter phonenumber">
        </b-form-input>
        </b-form-group>
        <b-form-group label="密码"
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
          localStorage.token = json.token
          store.commit('note_login_status',json.userName)
          alert("Login Success !")
          router.push('index')
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


\
