<template>
    <div class="menu-item">
        <div class="menu-item__control">
            <input type="button" class="hidden">
            <button type="button" class="delete-btn"><img src="@/assets/icons/delete-task-proj-icon.webp"></button>
        </div>
        <div class="menu-item__preview">
            <div class="preview">
                <div class="preview__control">
                    <button type="button" class="add-btn"><img src="@/assets/icons/upload-task-pic.webp"></button>
                    <input type="file" class="hidden">
                    <button type="button" class="delete-btn"><img src="@/assets/icons/delete-task-pic.webp"></button>
                </div>
                <div class="preview__picture">
                    <img @click="$router.push(`/project/${project.id_project}`)" :src="project.picture" alt="Изображение проекта">
                </div>
            </div>
        </div>
        <div class="menu-item__name">
            <input class="name" v-model="project.name">
        </div>
        <div class="menu-item__description">
            <textarea>{{ project.description }}</textarea>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ProjectMenuItem',
    props: {
        project: {
            type: Object,
            required: true
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
</style>