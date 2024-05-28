import { createStore } from 'vuex'
import users from './modules/users'
import tasks_solo from './modules/tasks_solo'
import projects from './modules/projects'
import tasks_proj from './modules/tasks_proj'
import members from './modules/members'
import documents from './modules/documents'

export default createStore({
  state: {
    
  },
  getters: {
    
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    users,
    tasks_solo,
    projects,
    tasks_proj,
    members,
    documents,
  }
})
