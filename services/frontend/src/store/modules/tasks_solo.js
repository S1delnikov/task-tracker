import axios from 'axios'
import router from '@/router'

export default {
    state: () => ( {
        tasks: [],
    }),
    getters: {
        getTasks(state) {
            return state.tasks
        }
    },
    mutations: {
        setTasks(state, tasks) {
            state.tasks = tasks
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

                ctx.commit('setTasks', tasks)
            } catch {
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