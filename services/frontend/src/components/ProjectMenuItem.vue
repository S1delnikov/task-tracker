<template>
    <div class="menu-item">
        <div class="menu-item__control">
            <input type="button" class="hidden">
            <button type="button" class="delete-btn" v-if="project.role=='owner'" @click="delProject(project.id_project)"><img src="@/assets/icons/delete-task-proj-icon.webp"></button>
            <button type="button" class="delete-btn" v-if="project.role!='owner'" @click="leaveFromProject(project.id_project)"><img src="@/assets/icons/delete-task-proj-icon.webp"></button>
        </div>
        <div class="menu-item__preview">
            <div class="preview">
                <div class="preview__control" v-if="project.role=='owner'">
                    <button type="button" class="add-btn"><img src="@/assets/icons/upload-task-pic.webp" @click="openFileDialog(project.id_project)"></button>
                    <input type="file" accept="image/*" class="hidden" :id="`upload-proj-pic_${project.id_project}`" @change="uploadProjectPic({'id_project': project.id_project, 'file': $event.target.files[0]})">
                    <button type="button" class="delete-btn" v-if="!project.picture.includes('/images/default/project_pic/project_pic.jpg')" @click="deleteProjectPic(project.id_project)"><img src="@/assets/icons/delete-task-pic.webp"></button>
                </div>
                <div class="preview__picture">
                    <img @click="$router.push(`/project/${project.id_project}`)" :src="project.picture" alt="Изображение проекта">
                </div>
            </div>
        </div>
        <div class="menu-item__name">
            <input class="name" v-model="project.name" :disabled="project.role!='owner'" @change="updateProject(project)">
        </div>
        <div class="menu-item__description">
            <textarea v-model="project.description" :disabled="project.role!='owner'" @change="updateProject(project)"></textarea>
        </div>
    </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
    name: 'ProjectMenuItem',
    props: {
        project: {
            type: Object,
            required: true
        }
    },
    methods: {
        ...mapActions(['updateProject', 'deleteProject', 'leaveProject', 'uploadProjectPic', 'deleteProjectPic']),
        delProject(id_project) {
            let capibara = prompt('Для удаления проекта введите слово "Капибара".', '');
            if (capibara != "Капибара" && capibara != null) {
                alert('Ошибка удаления. Попробуйте снова.')
            }
            else if (capibara=="Капибара") {
                this.deleteProject(id_project)              
            }
        },
        leaveFromProject(id_project) {
            let iWantLeave = confirm("Вы действительно хотите покинуть данный проект?")
            if (iWantLeave) {
                this.leaveProject(id_project)
            }
        },
        openFileDialog(id_project) {
            let fileDialog = document.getElementById(`upload-proj-pic_${id_project}`)
            fileDialog.click()
        }
    }
}
</script>

<style scoped>
.menu-item {
    background-color: #EDF5E1;
    width: 35%;
    padding: 2rem;
    border-radius: 3rem;
}

.menu-item__control {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
    margin-right: 0.2rem;
}

.menu-item__preview {
    width: 100%;
    /* overflow: hidden; */
    /* display: block; */
    margin: 0 auto;
}

.preview {
    width: 100%;
    /* border: 0.1rem solid #000; */
}

.preview:hover {
    cursor: pointer;
}

.preview__control {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.preview__picture img{
    display: block;
    margin: 0 auto;
    width: 90%;
    border-radius: 2rem;
}

.menu-item__name {
    font-size: 1.8rem;
    font-weight: 500;
    padding-top: 1rem;
    margin-bottom: 1rem;
}

.menu-item__name input {
    background-color: #E6ECDC;
    text-align: center;
    border: none;
    width: 100%;
    padding-left: 1rem;
    padding-right: 1rem;
}

.menu-item__name input:focus {
    outline: 0.2rem solid #ccd1c5;
}

.name {
    font-size: 2.6rem;
    text-wrap: nowrap;
    overflow: scroll;
    text-overflow: ellipsis;
}

.menu-item__description {
    display: block;
    margin: 0 auto;
    background-color: #fff;
}

.menu-item__description textarea {
    padding: 1rem;
    resize: none;
    width: 100%;
    height: 10rem;
    font-size: 1.4rem;
    text-align: justify;
    line-height: 2.0rem;
    overflow-x: hidden;
    background-color: #E6ECDC;
    border: 0.1rem solid #ccd1c5;
    border-radius: 1rem;
}

.menu-item__description textarea:focus {
    outline: 0.2rem solid #ccd1c5;
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

.add-btn:hover {
    background-color: #a4f3c2;
}

.delete-btn:hover {
    background-color: #ffd8d8;
}

button {
    background-color: #E6ECDC;
    border: none;
}   

button > img{
    display: block;
    padding: auto;
}

@media (max-width: 1024px) {
    .menu-item {
        width: 45%;
    }

    .name {
        font-size: 1.8rem;
    }

    .menu-item__description textarea {
        font-size: 1.6rem;
    }
}

@media (max-width: 768px) {
    .menu-item {
        width: 95%;
    }

    .name {
        font-size: 1.6rem;
    }

    .menu-item__description textarea {
        font-size: 1.2rem;
    }
}
</style>