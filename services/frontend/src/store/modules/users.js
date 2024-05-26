import axios from 'axios'
import router from '@/router'
import { useAttrs } from 'vue'
import { routeLocationKey } from 'vue-router'
import { reactive } from 'vue'

import { state } from '../index'

export default {
    state: {
        isAuth: false,
        username: '',
        profilePic: '',
        currentUser: '',
        currentUserRights: '',
    },
    getters: {
        getAuth(state) {
            return state.isAuth
            // console.log(localStorage.getItem('isAuthenticated'))
            // return localStorage.getItem('isAuthenticated')
        },
        getProfilePic(state) {
            // console.log('getters: ', state.profilePic.path)
            return state.profilePic
        },
        getCurrentUser(state) {
            return state.currentUser
        },
        getCurrentUserRights(state) {
            return state.currentUserRights
        }
    },
    mutations: {
        setAuth(state, value) {
            state.isAuth = value
        },
        setCurrentUser(state, currentUser) {
            state.currentUser = currentUser
        },
        setCurrentUserRights(state, currentUserRights) {
            state.currentUserRights = currentUserRights
        },
        logout(state) {
            localStorage.removeItem('token')
            localStorage.removeItem('username');
            localStorage.setItem('isAuthenticated', false);
            state.isAuth = false
        },
        setProfilePic(state, picture) {
            state.profilePic = picture
        }
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
            else {
                localStorage.setItem('isAuthenticated', false)
                router.push('/')
            }
        },
        async loadProfilePic(ctx) {
            try {
                const res = await axios.get('/get_profile_pic', {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }, 
                    responseType: 'blob' 
                })
                console.log(res.data)
                // console.log(new Blob([res.data.profile_pic], {type: res.data.profile_pic.media_type}))
                // const blob = await res.data.blob()
                // const url = URL.createObjectURL(res.data)

                const url = URL.createObjectURL(res.data)
                // return url;

                // const pic = await res.data.profile_pic

                console.log('actions: ', url)
                // console.log(typeof(pic))
                ctx.commit('setProfilePic', url)
            } catch(e) {
                console.log(e)
            }
        },
        async fetchCurrentUser(ctx) {
            try {
                const res = await axios.get('/about', {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                const currentUser = res.data
                ctx.commit('setCurrentUser', currentUser)
            } catch(e) {
                localStorage.setItem('isAuthenticated', false)
                router.push('/')
            }
        },
        async fetchCurrentUserRights(ctx, id_project) {
            try {
                const res = await axios.get(`/about/${id_project}`, {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                const currentUserRights = await res.data.rights
                ctx.commit('setCurrentUserRights', currentUserRights)
            } catch(e) {
                localStorage.setItem('isAuthenticated', false)
                router.push('/')
            }
        },
    }
}