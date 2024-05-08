import axios from 'axios'
import router from '@/router'
import { useAttrs } from 'vue'
import { routeLocationKey } from 'vue-router'

import { state } from '../index'

export default {
    state: {
        isAuth: false,
        username: '',
    },
    getters: {
        getAuth(state) {
            return state.isAuth
            // console.log(localStorage.getItem('isAuthenticated'))
            // return localStorage.getItem('isAuthenticated')
          }
    },
    mutations: {
        setAuth(state, value) {
            state.isAuth = value
        },
        logout(state) {
            localStorage.removeItem('token')
            localStorage.removeItem('username');
            localStorage.setItem('isAuthenticated', false);
            state.isAuth = false
        },
    },
    actions: {
        async login(ctx, form) {
            if (form.login != '' && form.password != ''){
                try{
                const User = new FormData();
                User.append('username', form.login);
                User.append('password', form.password);
                const token = await axios.post('login', User);
                localStorage.setItem("token", token.data.access_token);
                localStorage.setItem('username', form.login);
                localStorage.setItem('isAuthenticated', true);
            
                ctx.commit('setAuth', true)

                router.push('/');
                } catch(e) {
                  alert('Неправильный логин или пароль!');
                  ctx.commit('setAuthenticated', false)
                }
            }
            else {
                alert('Заполните все поля, чтобы продолжить')
              }
        },
        checkAuth(ctx) {
            if (localStorage.getItem('isAuthenticated') == 'true') {
                ctx.commit('setAuth', true)
            } 
        }
    }
}