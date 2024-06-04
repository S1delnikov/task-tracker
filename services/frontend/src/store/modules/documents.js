import axios from 'axios'
import router from '@/router'
import { reactive } from 'vue'


export default {
    state: () => ({
        host: process.env.VUE_APP_FASTAPI_BACKEND_URL,
        documents: [],
        usersWithAccess: [],
    }),
    getters: {
        getDocuments(state) {
            return state.documents
        },
        getUsersWithAccess(state) {
            return state.usersWithAccess
        }
    },
    mutations: {
        setDocuments(state, documents) {
            documents.forEach(doc => {
                doc.path = state.host + doc.path
            });
            state.documents = documents
        },
        addDocument(state, document) {
            document.path = state.host + document.path
            state.documents.push(document)
        },
        updateDocumentName(state, data) {
            state.documents.forEach(doc => {
                if (doc.id_document == data.id_document) {
                    doc.name = data.new_name
                }
            })
        },
        deleteDocument(state, id_document) {
            state.documents = state.documents.filter(document => document.id_document != id_document)
        },
        setUsersWithAccess(state, usersWithAccess) {
            state.usersWithAccess = usersWithAccess
        },
        addUserWithAccess(state, newUserWithAccess) {
            state.usersWithAccess.push(newUserWithAccess)
        },
        takeAwayAccess(state, id_user) {
            state.usersWithAccess = state.usersWithAccess.filter(user => user.id_user != id_user)
        },
    },
    actions: {
        async fetchAllDocuments(ctx) {
            try {
                const res = await axios.get('/get_documents', {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                const documents = await res.data.documents
                ctx.commit('setDocuments', documents)
            } catch(e) {
                if (e.response.status == 401) {
                    localStorage.setItem('isAuthenticated', false)
                    router.push('/')
                }
            }
        },
        async uploadDocument(ctx) {
            try {
                const file = new FormData()
                let endPoint
                if (event.target.files.length==1) {
                    file.append('document', event.target.files[0])
                    endPoint = '/upload_document'
                }
                else {
                    for (let i = 0; i <  event.target.files.length; i++) {
                        file.append('documents', event.target.files[i]);
                    }
                    endPoint = '/upload_documents'
                }
                const res = await axios.post(
                    endPoint,
                    file,
                    {
                        headers: {
                            Authorization: 'Bearer ' + localStorage.getItem('token')
                        }
                    }
                )
                const document = await res.data.document
                document.role = await res.data.user_document.role
                ctx.commit('addDocument', document)
            } catch(e) {
                if (e.response.status == 401) {
                    localStorage.setItem('isAuthenticated', false)
                    router.push('/')
                }
            }
        },
        async updateDocumentName(ctx, data) {
            try {
                await axios.put(`/update_document_name/${data.id_document}/${data.new_name}`, {}, {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                
                ctx.commit('updateDocumentName', data)
                
            } catch(e) {
                if (e.response.status == 401) {
                    localStorage.setItem('isAuthenticated', false)
                    router.push('/')
                }
            }
        },
        async fetchUsersWithAccess(ctx, id_document) {
            try {
                const res = await axios.get(
                    `/get_document_users/${id_document}`, {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                const usersWithAccess  = res.data.users
                ctx.commit('setUsersWithAccess', usersWithAccess)
            } catch(e) {
                if (e.response.status == 401) {
                    localStorage.setItem('isAuthenticated', false)
                    router.push('/')
                }
            }
        },
        async shareDocument(ctx, data) {
            try {
                const res = await axios.post(`/share_document/${data.id_document}/${data.new_user}`, {}, {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                const user = await res.data
                const newUserWithAccess = {'id_user': user.id_user, 'searchname': user.searchname, 'full_name': user.full_name}
                ctx.commit('addUserWithAccess', newUserWithAccess)
                if (res.status == 200){
                    let search = document.getElementById('search-document-member')
                    search.value = ''
                    search.style.border = '0.1rem solid #ccd1c5'
                }
            } catch(e) {
                if (e.response.status == 400) {
                    let search = document.getElementById('search-document-member')
                    search.style.border = '0.1rem solid red'
                    alert('Пользователь не найден.')
                }
                if (e.response.status == 401) {
                    localStorage.setItem('isAuthenticated', false)
                    router.push('/')
                }
            }
        },
        async takeAwayAccess(ctx, data) {
            try {
                await axios.delete(`/take_away_access/${data.id_document}/${data.id_user}`, {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                .then(
                    ctx.commit('takeAwayAccess', data.id_user)
                )

            } catch(e) {
                if (e.response.status == 401) {
                    localStorage.setItem('isAuthenticated', false)
                    router.push('/')
                }
            }
        },
        async deleteDocument(ctx, id_document) {
            try {
                await axios.delete(`/delete_document/${id_document}`, {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                .then(
                    ctx.commit('deleteDocument', id_document)
                )
            } catch(e) {
                if (e.response.status == 401) {
                    localStorage.setItem('isAuthenticated', false)
                    router.push('/')
                }
            }
        },
        async refuseDocument(ctx, id_document) {
            try {
                const res = await axios.delete(`/refuse_the_document/${id_document}`, {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('token')
                    }
                })
                .then(
                    ctx.commit('deleteDocument', id_document)
                )
            } catch(e) {
                if (e.response.status == 401) {
                    localStorage.setItem('isAuthenticated', false)
                    router.push('/')
                }
            }
        },
    }
}