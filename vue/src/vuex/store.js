import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)

const store = new Vuex.Store({
    state:{
        userName:'',
        token:''
    },
    mutations:{
        note_login_status(state,userName){
            localStorage.userName = userName
            state.userName = userName
            state.token = localStorage.token
        },
        clear_login_status(state){
            localStorage.clear()
            state.userName = ''
            state.token = ''
            console.log(state)
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
