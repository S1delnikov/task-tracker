<template>
    <div class="checklists">
        <button v-if="getAuth" class="create-checklist" type="button" @click="createTask">Добавить чеклист</button>
        <div v-if="getAuth" @mouseover="redraw" @touchmove="redraw" @playing="redraw" class="content" v-masonry="containerId" transition-duration="0.4s" item-selector=".item" stagger="0.03s">
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
        ...mapActions(['checkAuth', 'fetchCurrentUser', 'fetchAllTasks', 'createTask', 'loadProfilePic']),
        handleEmit(title) {
            console.log(title)
        },
        redraw() {        
            this.$redrawVueMasonry(this.containerId)
        }
    },
    mounted() {
        this.fetchCurrentUser()
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

.checklists {
    overflow: hidden;
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
    /* overflow: hidden; */
}

@media (max-width: 1600px) {
    .checklists {
        margin-left: 8rem;
    }

    .checklist {
        margin: 2rem;
    }
}

@media (max-width: 1280px) {
    .checklists {
        margin-left: 6rem;
    }

    .checklist {
        margin: 1rem;
    }
}

@media (max-width: 1024px) {
    .checklists {
        margin: auto;
    }

    .checklist {
        margin: 0.4rem;
    }
}

@media (max-width: 768px) {
    .checklist {
        margin: 1rem;
    }
}
</style>