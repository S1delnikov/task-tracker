<template>
    <div class="checklists">
        <h1>Checklists view</h1>
        <div v-if="getAuth" class="content">
            <!-- <Checklist class="checklist"></Checklist>
            <Checklist class="checklist"></Checklist>
            <Checklist class="checklist"></Checklist>
            <Checklist class="checklist"></Checklist>
            <Checklist class="checklist"></Checklist>
            <Checklist class="checklist"></Checklist>
            <Checklist class="checklist"></Checklist>
            <Checklist class="checklist"></Checklist> -->

            <Checklist v-for="task in getTasks" :key="task.id_task" v-bind:task="task" @test="handleEmit"></Checklist>
        </div>
        <div v-else>
            Нужно авторизоваться
        </div>
    </div>
</template>

<script>
import Checklist from "@/components/Checklist.vue"
import { mapActions, mapGetters } from 'vuex'
export default {
    name: 'Checklists',
    components: {
        Checklist
    },
    computed: {
        ...mapGetters(['getAuth', 'getTasks'])
    },
    methods: {
        ...mapActions(['checkAuth', 'fetchAllTasks']),
        handleEmit(title) {
            console.log(title)
        }
    },
    mounted() {
        this.checkAuth()
        this.fetchAllTasks()
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