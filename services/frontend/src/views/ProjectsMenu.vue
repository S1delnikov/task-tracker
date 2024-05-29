<template>
    <div class="projects">
        <div class="projects_create-btn">
            <button type="button">Создать проект</button>
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
        ...mapActions(['fetchAllProjects']),
        checkHost() {
            console.log(this.getHost)
        }
    },
    mounted() {
        this.fetchAllProjects()
    }
}
</script>

<style scoped>
/* .projects {
} */

.project {
    margin: auto 4rem;
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
    margin-left: 4rem;
}

.projects_create-btn button:hover {
    background-color: #318675;
}
</style>