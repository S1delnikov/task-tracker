<template>
    <div class="checklists">
        <h1>Checklists view</h1>
        <button v-if="getAuth" class="create-checklist" type="button">Добавить чеклист</button>

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

.create-checklist {
    font-size: 1.6rem;
    padding: 1.5rem;
    border: none;
    background-color: #379683;
    color: #8EE4AF;
    border-radius: 4rem;
    margin: 1rem auto;
    margin-left: 4rem;
}

.create-checklist:hover {
    background-color: #318675;
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