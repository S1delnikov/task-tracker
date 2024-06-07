<template>
    <div class="projects">
        <div class="projects_create-btn">
            <button type="button" @click="createProject">Создать проект</button>
        </div>
        <div class="projects__list">
            <ProjectMenuItem v-for="project in getProjects" :key="project.id_project" :project="project" class="project" />
        </div>
        <!-- <ProjectMenuItem @click="$router.push('/project')" class="project" />
        <ProjectMenuItem @click="$router.push('/project')" class="project" />
        <ProjectMenuItem @click="$router.push('/project')" class="project" /> -->
    </div>
</template>

<script>
import ProjectMenuItem from '@/components/ProjectMenuItem.vue'
import { mapGetters, mapActions } from 'vuex'
export default {
    name: 'ProjectsMenu',
    components: {
        ProjectMenuItem
    },
    computed: {...mapGetters(['getHost', 'getProjects'])},
    methods: {
        ...mapActions(['checkAuth', 'fetchCurrentUser', 'fetchAllProjects', 'createProject']),
        checkHost() {
            console.log(this.getHost)
        }
    },
    created() {
        this.checkAuth()
    },
    mounted() {
        this.fetchCurrentUser()
        this.fetchAllProjects()
    }
}
</script>

<style scoped>
/* .projects {
} */

.project {
    display: block;
    margin: auto;
    margin-bottom: 4rem;
}

.projects_create-btn button{
    font-size: 1.6rem;
    padding: 1.5rem;
    border: none;
    background-color: #379683;
    color: #8EE4AF;
    border-radius: 4rem;
    margin: 1rem auto;
    margin-left: 8%;
}

.projects_create-btn button:hover {
    background-color: #318675;
}

.projects__list {
    display: flex;
    flex-wrap: wrap;
}

@media (max-width:1600px) {
    .projects_create-btn button {
        margin-left: 9rem;
    }
}

@media (max-width:1280px) {
    .projects_create-btn button {
        margin-left: 7rem;
    }
}

@media (max-width:1024px) {
    .projects_create-btn button {
        margin-left: 2.5rem;
    }
}

@media (max-width: 768px) {
    .projects_create-btn button {
        display: block;
        margin: 1rem auto;
        max-width: 32rem;
    }
}
</style>