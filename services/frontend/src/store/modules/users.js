import axios from 'axios'
import router from '@/router'
// import { useAttrs } from 'vue'
// import { routeLocationKey } from 'vue-router'
import { reactive } from 'vue'

// import { state } from '../index'

export default {
    state: {
        isAuth: false,
        username: '',
        profilePic: '',
        currentUser: '',
        currentUserRights: '',
        host: 'http://127.0.0.1:8000',
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
            currentUser.picture = state.host + currentUser.picture
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
                const User = new FormData()
                User.append('username', form.login)
                User.append('password', form.password)
                const token = await axios.post('login', User)
                localStorage.setItem("token", token.data.access_token)
                localStorage.setItem('username', form.login)
                localStorage.setItem('isAuthenticated', true)
            
                ctx.commit('setAuth', true)

                // router.push('/')
                location.reload()
                } catch(e) {
                  alert('Неправильный логин или пароль!')
                  ctx.commit('setAuthenticated', false)
                }
            }
            else {
                alert('Заполните все поля, чтобы продолжить')
              }
        },
        async checkAuth(ctx) {
            const isAuth = localStorage.getItem('isAuthenticated')
            if (isAuth == 'true') {
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
                if (e.response.status == 401) {
                    localStorage.setItem('isAuthenticated', false)
                    router.push('/')
                }
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
                console.log(currentUser)
                ctx.commit('setCurrentUser', currentUser)
            } catch(e) {
                if (e.response.status == 401) {
                    localStorage.setItem('isAuthenticated', false)
                    router.push('/')
                }
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
                if (e.response.status == 401) {
                    localStorage.setItem('isAuthenticated', false)
                    router.push('/')
                }
            }
        },
        async updateUserInfo(ctx, currentUser) {
            try {
                console.log('start')
                const res = await axios.put('/update_user_info', 
                {
                    "searchname": currentUser.searchname,
                    "full_name": currentUser.full_name,
                    "disabled": currentUser.disabled
                },
                {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                }
                )
                const updatedUser = await res.data
                ctx.commit('setCurrentUser', updatedUser)
            } catch(e) {
                if (e.response.status == 400) {
                    alert('Данный идентификатор уже занят, попробуйте другой.')
                }
                if (e.response.status == 401) {
                    localStorage.setItem('isAuthenticated', false)
                    router.push('/')
                }
            }
        },
        async uploadProfilePic(ctx) {
            try {
                const file = new FormData()
                file.append('picture', event.target.files[0])
                const res = await axios.post('/upload_profile_pic', file, {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                const userWithNewPicture = await res.data
                ctx.commit('setCurrentUser', userWithNewPicture)
            } catch(e) {
                if (e.response.status == 401) {
                    localStorage.setItem('isAuthenticated', false)
                    router.push('/')
                }
            }
        },
        async deleteProfilePic(ctx) {
            try {
                const res = await axios.delete('/delete_profile_pic', {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                const userWithoutPicture = await res.data
                ctx.commit('setCurrentUser', userWithoutPicture)
            } catch(e) {
                if (e.response.status == 401) {
                    localStorage.setItem('isAuthenticated', false)
                    router.push('/')
                }
            }
        }
    }
}