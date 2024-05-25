import axios from 'axios'
import router from '@/router'

export default {
    state: () => ( {
        projects: [],
        host: 'http://127.0.0.1:8000'
    }),
    getters: {
        getProjects(state) {
            return state.projects
        },
        getHost(state) {
            return state.host
        }
    },
    mutations: {
        setProjects(state, projects) {
            projects.forEach(p => {
                p.picture = state.host + p.picture
            })
            state.projects = projects
        }
    },
    actions: {
        async fetchAllProjects(ctx) {
            try {
                const res  = await axios.get(
                    '/get_projects',{
                        headers: {
                            Authorization: 'Bearer ' + localStorage.getItem('token')
                        }
                    })
                const projects = await res.data
                ctx.commit('setProjects', projects)
                console.log(projects)
            } catch(e) {
                // console.log(e)
                localStorage.setItem('isAuthenticated', false)
                router.push('/')
            }
        }
    }
}