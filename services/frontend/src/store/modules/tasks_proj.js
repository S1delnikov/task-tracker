import axios from 'axios'
import router from '@/router'
import { reactive } from 'vue'

export default {
    state: () => ({
        tasksProj: [],
        host: 'http://127.0.0.1:8000',
        id_project: '',
    }),
    getters: {
        getTasksProj(state) {
            return state.tasksProj
        },
    },
    mutations: {
        setIdProject(state, id_project) {
            state.id_project = id_project
        },
        setTasksProj(state, tasksProj) {
            tasksProj.forEach(t => {
                t.picture = state.host + t.picture
            })
            state.tasksProj = tasksProj
        },
        createTaskProj(state, newTask) {
            state.tasksProj.push(newTask)
        },
        updateTaskProj(state, taskProj) {
            state.tasksProj.forEach(t => {
                if (t.id_task == taskProj.id_task) {
                    t = taskProj
                }
            })
            console.log(state.tasksProj)
        },
        deleteTaskProj(state, id_task) {
            state.tasksProj = state.tasksProj.filter(task => task.id_task != id_task)
        },
        updateTaskProjPicAndCategory(state, taskProj) {
            state.tasksProj.forEach(t => {
                if (t.id_task == taskProj.id_task) {
                    t.picture = state.host + taskProj.picture
                    t = taskProj
                }
            })
        },
        createSubtaskProj(state, data) {
            state.tasksProj.forEach(task => {
                if (task.id_task == data.task.id_task) {
                    task.subtasks.push(data.subtask)
                }
            })
        },
        updateSubtaskProj(state, stask) {
            state.tasksProj.forEach(task => {
                task.subtasks.forEach(subtask => {
                    if (subtask.id_subtask == stask.id_subtask) {
                        subtask = stask
                    }
                })
            })
        },
        deleteSubtaskProj(state, stask) {
            state.tasksProj.forEach(task => {
                task.subtasks = task.subtasks.filter(subtask => subtask.id_subtask != stask.id_subtask)
            })
        },
    },
    actions: {
        async fetchAllTasksProj(ctx, id_project) {
            try {
                const res = await axios.get(`/get_proj_tasks/${id_project}`, {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                const tasksProj = res.data
                ctx.commit('setTasksProj', tasksProj)
            } catch(e) {
                localStorage.setItem('isAuthenticated', false)
                router.push('/')
            }
        },
        async createTaskProj(ctx, id_project) {
            try {
                const res = await axios.post(
                    `/create_task_proj/${id_project}`, 
                    {
                        title: '',
                        description: '',
                        start_date: Date.now(),
                        end_date: Date.now(),
                        done: false,
                        rank: '',
                        category: "Надо сделать"
                    },
                    {
                        headers: 
                        {
                            Authorization: 'Bearer ' + localStorage.getItem('token')
                        }
                    }
                )
                const newTask = await res.data
                ctx.commit('createTaskProj', newTask)
            } catch(e) {
                console.log(e)
                if (e.response.status == 401) {
                    localStorage.setItem('isAuthenticated', false)
                    router.push('/')
                }
            }
        },
        async updateTaskProj(ctx, data) {
            console.log('id', data.id_project, 'task', data.taskProj)
            try {
                await axios.put(
                    `/update_task_proj/${data.id_project}/${data.taskProj.id_task}`, 
                    data.taskProj, 
                    {
                        headers: {
                            Authorization: 'Bearer ' + localStorage.getItem('token')
                        }
                    }
                )
                ctx.commit('updateTaskProj', data.taskProj)

            } catch(e) {
                console.log(e)
                alert('Такой задачи не существует.')
            }
        },
        async deleteTaskProj(ctx, data) {
            try {
                await axios.delete(
                    `/delete_task_proj/${data.id_project}/${data.taskProj.id_task}`,
                    {
                        headers: 
                        {
                            Authorization: 'Bearer ' + localStorage.getItem('token')
                        }
                    }
                )
                ctx.commit('deleteTaskProj', data.taskProj.id_task)
            } catch(e) {
                console.log(e)
                if (e.response.status == 401) {
                    localStorage.setItem('isAuthenticated', false)
                    router.push('/')
                }
            }
        },
        async uploadTaskProjectPic(ctx, data) {
            try {
                const file = new FormData()
                file.append('picture', event.target.files[0])
                const res = await axios.post(
                    `/upload_task_pic/${data.id_project}/${data.taskProj.id_task}`,
                    file,
                    {
                        headers: {
                            Authorization: 'Bearer ' + localStorage.getItem('token')
                        }
                    }
                )
                const taskProj = await res.data
                console.log('res', taskProj)
                ctx.commit('updateTaskProjPicAndCategory', taskProj)
            } catch(e) {
                if (e.response.status == 400) {
                    alert('Недопустимый тип файла.')
                }
                else if (e.response.status == 401) {
                    localStorage.setItem('isAuthenticated', false)
                    router.push('/')
                }
            }
        },
        async deleteTaskProjectPic(ctx, data) {
            try {
                const res = await axios.delete(
                    `/delete_task_pic/${data.id_project}/${data.taskProj.id_task}`,
                    {
                        headers: {
                            Authorization: 'Bearer ' + localStorage.getItem('token')
                        }
                    }
                )
                const taskProj = await res.data
                ctx.commit('updateTaskProjPicAndCategory', taskProj)
            } catch(e) {
                localStorage.setItem('isAuthenticated', false)
                router.push('/')
            }
        },
        async changeTaskProjCategory(ctx, data) {
            try {
                console.log('data', data.taskProj.category)
                data.taskProj.category = data.category
                const res = await axios.put(
                    `/update_task_proj/${data.id_project}/${data.taskProj.id_task}`, 
                    data.taskProj, 
                    {
                        headers: {
                            Authorization: 'Bearer ' + localStorage.getItem('token')
                        }
                    }
                )
                const taskProj = await res.data
                ctx.commit('updateTaskProjPicAndCategory', taskProj)
            } catch(e) {
                if (e.response.status == 401) {
                    localStorage.setItem('isAuthenticated', false)
                    router.push('/')
                }
            }
        },
        async createSubtaskProj(ctx, task){
            try {
                const res = await axios.post(
                    `create_subtask/${task.id_task}/`, 
                    {
                        title: '',
                        description: '',
                        done: false
                    }, 
                    {
                        headers: {
                            Authorization: 'Bearer ' + localStorage.getItem('token')
                        }
                })
                const new_subtask = await res.data
                const subtask =  {
                    description: new_subtask.description,
                    done: new_subtask.done,
                    id_subtask: new_subtask.id_subtask,
                    title: new_subtask.title,
                }
                ctx.commit('createSubtaskProj', { subtask, task })
            } catch(e) {
                localStorage.setItem('isAuthenticated', false)
                router.push('/')
            }
        },
        async updateSubtaskProj(ctx, subtask) {
            try {
                await axios.put(`/update_subtask/${subtask.id_subtask}/`, subtask, {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                ctx.commit('updateSubtaskProj', subtask)
            } catch(e) {
                localStorage.setItem('isAuthenticated', false)
                router.push('/')
            }
        },
        async deleteSubtaskProj(ctx, subtask) {
            try {
                await axios.delete(`/delete_subtask/${subtask.id_subtask}/`, {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                ctx.commit('deleteSubtaskProj', subtask)
            } catch(e) {
                localStorage.setItem('isAuthenticated', false)
                router.push('/')
            }
        }
    }
}