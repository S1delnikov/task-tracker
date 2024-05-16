<template>
    <div class="checklists">
        <h1>Checklists view</h1>
        <button v-if="getAuth" class="create-checklist" type="button" @click="createTask">Добавить чеклист</button>
        <button v-if="getAuth" type="button" @click="loadProfilePic">Картинка</button>
        <img v-if="getAuth" :src="getProfilePic" alt="">
        <img src="https://via.placeholder.com/600/92c952" alt="">
        <div v-if="getAuth" @mouseover="redraw" class="content" v-masonry="containerId" transition-duration="0.4s" item-selector=".item" stagger="0.03s">
            <!-- <Checklist class="checklist"></Checklist>
            <Checklist class="checklist"></Checklist>
            <Checklist class="checklist"></Checklist>
            <Checklist class="checklist"></Checklist>
            <Checklist class="checklist"></Checklist>
            <Checklist class="checklist"></Checklist>
            <Checklist class="checklist"></Checklist>
            <Checklist class="checklist"></Checklist> -->
            <Checklist v-masonry-tile class="item" v-for="task in getTasks" :key="task.id_task" v-bind:task="task" @test="handleEmit"></Checklist>
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
    data: () => ({
        containerId: 'containerId'
    }),
    components: {
        Checklist
    },
    computed: {
        ...mapGetters(['getAuth', 'getTasks', 'getProfilePic'])
    },
    methods: {
        ...mapActions(['checkAuth', 'fetchAllTasks', 'createTask', 'loadProfilePic']),
        handleEmit(title) {
            console.log(title)
        },
        redraw() {        
            this.$redrawVueMasonry(this.containerId)
        }
    },
    mounted() {
        this.checkAuth()
        this.fetchAllTasks()
    },
    updated() {
        this.redraw()
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

.item {
    margin-bottom: 1rem;
}

.checklist {
    margin: auto 4rem;
    margin-bottom: 4rem;
}
</style>