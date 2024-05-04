<template>
    <div class="checklists">
        <h1>Checklists view</h1>
        <div class="content">
            <Checklist class="checklist"></Checklist>
            <Checklist class="checklist"></Checklist>
            <Checklist class="checklist"></Checklist>
            <Checklist class="checklist"></Checklist>
            <Checklist class="checklist"></Checklist>
            <Checklist class="checklist"></Checklist>
            <Checklist class="checklist"></Checklist>
            <Checklist class="checklist"></Checklist>
        </div>
    </div>
</template>

<script>
import Checklist from "@/components/Checklist.vue"
export default {
    name: 'Checklists',
    components: {
        Checklist
    }
}
</script>

<style scoped>
h1 {
    font-size: 1.6rem;
}

.content {
    display: flex;
    flex-wrap: wrap;
    /* justify-content: space-between; */
}

.checklist {
    margin: auto 4rem;
    margin-bottom: 4rem;
}
</style>