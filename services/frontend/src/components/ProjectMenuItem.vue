<template>
    <div class="menu-item">
        <div class="menu-item__preview">
            <!-- <router-link to="" > -->
                <img class="preview" @click="$router.push(`/project/${project.id_project}`)" :src="project.picture" alt="Изображение проекта">
            <!-- </router-link> -->
        </div>
        <div class="menu-item__name">
            <h2 class="name">{{ project.name }}</h2>
        </div>
        <div class="menu-item__description">
            <p>{{ project.description }} Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequatur culpa et illo cupiditate necessitatibus nostrum quis delectus ratione quaerat deserunt. Nulla eum rerum iste delectus ut tempora sunt suscipit, corrupti quia iure voluptate ipsam beatae natus pariatur! Earum nobis minus provident modi, veritatis sit vel reiciendis omnis hic eius. Illum dicta, ipsa aspernatur perspiciatis repellendus voluptatem vel cumque, voluptates illo excepturi vitae quod! Saepe quia repudiandae nihil cumque pariatur facilis asperiores doloremque odit excepturi a totam, illum id sapiente nostrum, consequuntur numquam tempore veniam voluptates dolorem voluptatem dolor commodi alias? Aspernatur, maiores assumenda ea odio aliquid nostrum dolorum quis nobis.</p>
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

.menu-item__preview {
    width: fit-content;
    overflow: hidden;
    display: block;
    margin: 0 auto;
    background-color: antiquewhite;
}

.preview {
    width: 40rem;
    border: 0.1rem solid #000;
}

.menu-item__name {
    display: block;
    margin: 0 auto;
    margin-top: 0.5rem;
    margin-bottom: 1.5rem;
    text-align: center;
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
}
</style>