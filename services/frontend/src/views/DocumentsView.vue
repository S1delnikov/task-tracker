<template>
    <div class="documents">
        <div class="documents__control">
            <button type="button" @click="openFileDialog">Загрузить документ</button>
            <input type="file" class="hidden" id="file-picker" multiple @change="uploadDocument()">
        </div>
        <div class="documents__board">
            <div class="documets__list">
                <div class="document" v-for="document in getDocuments" :key="document.id_document">
                    <input type="text" :disabled="document.role!='owner'" v-model="document.name" :title="document.name" @change="updateDocumentName({'id_document': document.id_document, 'new_name': document.name})">
                    <button type="button" v-if="document.role=='owner'" @click="showDocumentControl(document.id_document)">Управление</button>
                    <div class="document__dialog hidden" @click="showDocumentControl(document.id_document)" :id="`docControl_${document.id_document}`">
                        <div @click.stop class="dialog__content">
                            <div class="dialog__search">
                                <input type="text" id="search-document-member" placeholder="Введите имя пользователя..." v-model="searchUsername">
                                <button type="button" @click="shareDocument({'id_document': document.id_document, 'new_user': searchUsername})">Добавить</button>
                            </div>
                            <div class="dialog__table">
                                <table>
                                    <thead>
                                        <tr>
                                            <th>Имя пользователя</th>
                                            <th>Действие</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="user in getUsersWithAccess" :key="user.id_user">
                                            <td>{{ user.full_name }}</td>
                                            <td><button class="search__button" @click="takeAwayAccess({'id_document': document.id_document, 'id_user': user.id_user})">Удалить</button></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <button class="dialog__delete-doc-btn" type="button" @click="deleteDocument(document.id_document)">Удалить документ</button>
                        </div>
                    </div>
                    <button type="button"><a :href="document.path" :download="document.name">Скачать</a></button>
                    <button type="button" v-if="document.role!='owner'" @click="refuseDocument(document.id_document)">Удалить</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'
export default {
    name: 'DocumentsView',
    data: () => ({
        dialogStatus: { },
        searchUsername: ''
    }),
    computed: {
        ...mapState(['documents']),
        ...mapGetters(['getDocuments', 'getUsersWithAccess'])
    },
    methods: {
        ...mapActions(['fetchAllDocuments', 'uploadDocument', 'deleteDocument', 'refuseDocument', 'updateDocumentName', 'fetchUsersWithAccess', 'shareDocument', 'takeAwayAccess']),
        openFileDialog() {
            let filePicker = document.getElementById('file-picker')
            filePicker.click()
        },
        async showDocumentControl(id_document) {
            await this.fetchUsersWithAccess(id_document)
            let dialog = document.getElementById(`docControl_${id_document}`)
            dialog.classList.toggle('hidden')
        },
    },
    created() {
        this.fetchAllDocuments()
        // console.log(this.dialogStatus)
        for (let doc of this.getDocuments) {
            this.dialogStatus[doc.id_document] = false
        }
        
    },
    mounted() {
        for (let doc of this.getDocuments) {
            this.dialogStatus[doc.id_document] = false
        }
        console.log(this.dialogStatus)
    },

}
</script>

<style scoped>
.documents__control {
    margin: 2rem;
}

.documents__control button {
    font-size: 1.6rem;
    padding: 1.5rem;
    border: none;
    background-color: #379683;
    color: #8EE4AF;
    border-radius: 4rem;
    margin: 1rem auto;
    margin-bottom: 0;
    margin-left: 1rem;
}

.documents__control button:hover {
    background-color: #318675;
}

.documents__control button {
    padding: 1rem;
    font-size: 1.8rem;
}

.documents__board {
    background-color: #EDF5E1;
    border-radius: 2rem;
    width: 65%;
    padding: 2rem 4rem;
    margin-left: 12%;
}

.documets__list {
    padding: 2rem;
}

.document {
    padding: 0.4rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
    background-color: #379683;
    border-radius: 1rem;
}

.document > input {
    width: 70%;
    font-size: 2.4rem;
    padding: 1rem;
    margin: 0.4rem;
    background-color: #379683;
    border: 0.1rem solid #8EE4AF;
    border-radius: 1rem;
    color: #8EE4AF;
}

.document > input:focus {
    outline: 0.1rem solid #8EE4AF
}

.document > button, button > a{
    width: auto;
    font-size: 1.8rem;
    padding: 0.5rem 1rem;
    background-color: #379683;
    color: #8EE4AF;
    border: none;
    text-decoration: none;
    margin-right: 0.5rem;
}

.document > button:hover {
    outline: 0.1rem solid #8EE4AF;
    border-radius: 1rem;
}

.document__dialog {
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
    background: rgba(0, 0, 0, 0.5);
    position: fixed;
    z-index: 1;
    display: flex;
}

.dialog__content {
    margin: auto;
    padding: 1rem;
    background-color: #EDF5E1;
    border-radius: 1.2rem;
    height: fit-content;
    width: 50%;
}

.hidden {
    opacity: 0;
    height: 0;
    width: 0;
    line-height: 0;
    overflow: hidden;
    padding: 0;
    margin: 0;
}

.dialog__search {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 1rem;
    padding-left: 0;
    padding-right: 0;
}

.dialog__search input {
    width: 80%;
    margin-right: 2rem;
    font-size: 1.6rem;
    background-color: #E6ECDC;
    border: none;
    border-radius: 1.2rem;
    padding: 1rem;
}

.dialog__search input:focus {
    outline: 0.2rem solid #ccd1c5;
}

.dialog__search button {
    padding: 0.8rem;
    font-size: 1.2rem;
    background-color: #e6ecdc;
    border: 0.1rem solid #ccd1c5;
    border-radius: 1.2rem;
}

.dialog__search button:hover {
    background-color: #ccd1c5;
}

.dialog__table {
    margin-left: 1rem;
    margin-bottom: 1rem;
    padding-left: 1rem;
    width: 90%;
}

.dialog__table table, th, td {
    text-align: center;
    border: 0.1rem solid #ccd1c5;
    border-collapse: collapse;
}

.dialog__table th {
    width: 100%;
    padding: 1rem;
    font-size: 1.4rem;
}

.dialog__table td {
    font-size: 1.2rem;
    padding: 1rem;
}

.dialog__delete-doc-btn {
    padding: 0.8rem;
    font-size: 1.2rem;
    background-color: #e6ecdc;
    border: 0.1rem solid #ccd1c5;
    border-radius: 1.2rem;
    margin-left: 2rem;
}

.dialog__delete-doc-btn:hover {
    background-color: #ccd1c5;
}
</style>