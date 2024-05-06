<template>
    <div class="projects">
        <ProjectMenuItem @click="$router.push('/project')" class="project" />
        <ProjectMenuItem @click="$router.push('/project')" class="project" />
        <ProjectMenuItem @click="$router.push('/project')" class="project" />
        <ProjectMenuItem @click="$router.push('/project')" class="project" />
    </div>
</template>

<script>
import ProjectMenuItem from '@/components/ProjectMenuItem.vue'
export default {
    name: 'ProjectsMenu',
    components: {
        ProjectMenuItem
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