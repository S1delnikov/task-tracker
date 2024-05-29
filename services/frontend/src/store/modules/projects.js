import axios from 'axios'
import router from '@/router'

export default {
    state: () => ( {
        projects: [],
        host: 'http://127.0.0.1:8000',
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
        },
        addProject(state, newProject) {
            newProject.picture = state.host + newProject.picture
            state.projects.push(newProject)
        },
        updateProject(state, updatedProject) {
            state.projects.forEach(project => {
                if (project.id_project == updatedProject.id_project) {
                    project = updatedProject                    
                }
            })
        },
        deleteProject(state, id_project) {
            state.projects = state.projects.filter(project => project.id_project != id_project)
        },
        updateProjPic(state, updatedProj) {
            state.projects.forEach(project => {
                if (project.id_project == updatedProj.id_project) {
                    project.picture = state.host + updatedProj.picture
                }
            })
        },
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
                if (e.response.status == 401) {
                    localStorage.setItem('isAuthenticated', false)
                    router.push('/')
                }
            }
        },
        async createProject(ctx) {
            try {
                const res = await axios.post('/create_proj', {'name': '', 'description': ''}, {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                const data = await res.data
                const newProject = {
                    'id_project': data.project.id_project,
                    'name': data.project.name,
                    'description': data.project.description,
                    'picture': data.project.picture,
                    'role': data.link_project_and_user.role
                }
                ctx.commit('addProject', newProject)
            } catch(e) {
                if (e.response.status == 401) {
                    localStorage.setItem('isAuthenticated', false)
                    router.push('/')
                }
            }
        },
        async updateProject(ctx, project) {
            try {
                const res = await axios.put(`/update_proj/${project.id_project}`, project, {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                const updatedProject = await res.data
                ctx.commit('updateProject', updatedProject)
            } catch(e) {
                if (e.response.status == 401) {
                    localStorage.setItem('isAuthenticated', false)
                    router.push('/')
                }
            }
        },
        async deleteProject(ctx, id_project) {
            try {
                await axios.delete(`/delete_proj/${id_project}`, {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                .then(
                    ctx.commit('deleteProject', id_project)
                )
            } catch(e) {
                if (e.response.status == 401) {
                    localStorage.setItem('isAuthenticated', false)
                    router.push('/')
                }
            }
        },
        async leaveProject(ctx, id_project) {
            try {
                await axios.delete(`/leave_proj/${id_project}`, {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                .then(
                    ctx.commit('deleteProject', id_project)
                )
            } catch {

            }
        },
        async uploadProjectPic(ctx, data) {
            try {
                const file = new FormData()
                file.append('picture', data.file)
                const res = await axios.post(`/upload_project_pic/${data.id_project}`, file, {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                const updatedProj = await res.data
                ctx.commit('updateProjPic', updatedProj)
            } catch(e) {
                if (e.response.status == 401) {
                    localStorage.setItem('isAuthenticated', false)
                    router.push('/')
                }
            }
        },
        async deleteProjectPic(ctx, id_project) {
            try {
                const res = await axios.delete(`/delete_project_pic/${id_project}`, {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                const updatedProj = await res.data
                ctx.commit('updateProjPic', updatedProj)
            } catch(e) {
                if (e.response.status == 401) {
                    localStorage.setItem('isAuthenticated', false)
                    router.push('/')
                }
            }
        },
    }
}