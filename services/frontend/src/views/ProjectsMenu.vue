<template>
    <div class="projects">
        <ProjectMenuItem v-for="project in getProjects" :key="project.id_project" :project="project" class="project" />
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
.projects {
    display: flex;
    flex-wrap: wrap;
}

.project {
    margin: auto 4rem;
    margin-bottom: 4rem;
}
</style>