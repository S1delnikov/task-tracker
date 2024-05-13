import axios from 'axios'
import router from '@/router'
import { reactive } from 'vue'

export default {
    state: () => ( {
        tasks: [],
        default_subtask: {
            title: '',
            description: '',
            done: false
        }
    }),
    getters: {
        getTasks(state) {
            return state.tasks
        },
        getDefaultSubtask(state) {
            return state.default_subtask
        }
    },
    mutations: {
        setTasks(state, tasks) {
            state.tasks = tasks
        },
        createTask(state, task){
            state.tasks.push(task)
        },
        updateTask(state, task) {
            state.tasks.forEach(t => {
                if (t.id_task == task.id_task) {
                    t = task
                }
            })
        },
        deleteTask(state, task) {
            state.tasks = state.tasks.filter(t => t.id_task != task.id_task)
        },
        createSubtask(state, data) {
            state.tasks.forEach(task => {
                if (task.id_task == data.task.id_task) {
                    task.subtasks.push(data.subtask)
                }
            })

        },
        updateSubtask(state, stask) {
            state.tasks.forEach(task => {
                task.subtasks.forEach(subtask => {
                    if (subtask.id_subtask == stask.id_subtask) {
                        subtask = stask
                    }
                })
            })
        },
        deleteSubtask(state, stask) {
            state.tasks.forEach(task => {
                task.subtasks = task.subtasks.filter(subtask => subtask.id_subtask != stask.id_subtask)
            })
        }
    },
    actions: {
        async fetchAllTasks(ctx) {
            try {
                const res = await axios.get('/get_solo_tasks', {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                const tasks = await res.data
                console.log(tasks)
                ctx.commit('setTasks', tasks)
            } catch {
                localStorage.setItem('isAuthenticated', false)
                router.push('/')
            }
        },
        async createTask(ctx) {
            try{
                const res = await axios.post(
                        `create_task_solo`, 
                        {
                            title: '',
                            description: '',
                            start_date: Date.now(),
                            end_date: Date.now(),
                            done: false
                        }, 
                        {
                            headers: {
                                Authorization: 'Bearer ' + localStorage.getItem('token')
                            }
                        }
                    )
                const new_task = await res.data
                const task = {
                    id_task: new_task.id_task,
                    title: new_task.title,
                    description: new_task.description,
                    start_date: new_task.start_date,
                    end_date: new_task.end_date,
                    done: new_task.done,
                    subtasks: []
                }
                ctx.commit('createTask', task)
            } catch(e) {
                localStorage.setItem('isAuthenticated', false)
                router.push('/')
            }
        },
        async updateTask(ctx, task) {
            try {
                await axios.put(`/update_task_solo/${task.id_task}/`, task, {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                ctx.commit('updateTask', task)
            } catch(e) {
                alert('Такой задачи не существует.')
            }
        },
        async deleteTask(ctx, task) {
            try{
                await axios.delete(`/delete_task_solo/${task.id_task}/`, {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                ctx.commit('deleteTask', task)
            } catch(e) {
                alert('Такой задачи не существует.')
            }
        },
        async createSubtask(ctx, task){
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
                ctx.commit('createSubtask', { subtask, task })
                // ctx.dispatch('fetchAllTasks')
            } catch(e) {
                alert('Такой задачи не существует.')
            }
        },
        async updateSubtask(ctx, subtask) {
            try {
                await axios.put(`/update_subtask/${subtask.id_subtask}/`, subtask, {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                ctx.commit('updateSubtask', subtask)
            } catch(e) {
                alert('Такой подзадачи не существует.')
            }
        },
        async deleteSubtask(ctx, subtask) {
            try {
                await axios.delete(`/delete_subtask/${subtask.id_subtask}/`, {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                ctx.commit('deleteSubtask', subtask)
            } catch(e) {
                alert('Такой подзадачи не существует.')
            }
        }
    }
}