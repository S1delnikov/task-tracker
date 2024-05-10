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
        async updateSubtask(ctx, subtask) {
            try {
                await axios.put(`/update_subtask/${subtask.id_subtask}/`, subtask, {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
            } catch(e) {
                alert('Такой подзадачи не существует.')
            }
        }
    }
}