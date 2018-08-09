import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)

const store = new Vuex.Store({
    state:{
        userName:'',
        token:''
    },
    mutations:{
        note_login_status(state,userName,token){
            console.log(userName)
            localStorage.userName = userName
            console.log(token)
            localStorage.token = token
            state.userName = userName
            state.token = token
        },
        clear_login_status(state){
            localStorage.clear()
            state.userName = ''
            state.token = ''
        }
    },
    getters:{
        read_login_status(state){
            if(state.token === ''){
                state.userName = localStorage.userName
                state.token = localStorage.token
            }
            return state
        }
    }
})

export default store
