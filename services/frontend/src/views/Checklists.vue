<template>
    <div class="checklists">
        <button v-if="getAuth" class="create-checklist" type="button" @click="createTask">Добавить чеклист</button>
        <!-- <button v-if="getAuth" type="button" @click="loadProfilePic">Картинка</button>
        <img v-if="getAuth" :src="getProfilePic" alt="">
        <img src="http://127.0.0.1:8000/static/qwerty.jpg" alt="" srcset="">
        <img src="http://127.0.0.1:8000/static/pepe.jpeg" alt="" srcset="">
        <img src="https://sun1-91.userapi.com/impg/M3CmYvxNZjaJXL0ylFV-pFLVyaR4LPSoYe0GWA/9K4feptusnU.jpg?size=792x1118&quality=95&sign=36636e9b884c8952192e7c61d67777d3&type=album" alt="" srcset="">
        <img src="https://sun9-22.userapi.com/impg/DVhZ9Puv2Ba30KZ1qhYotx9Iz6nalRKsJ04S5A/oMoy6286i4U.jpg?size=406x604&quality=96&sign=0a75add7ef1cc2e4c73c9130be0243be&type=album" alt="" srcset="">
        <img src="https://www.dropbox.com/scl/fi/uk39eg1mtp2pm34vsjdvp/antarctica3.jpg?rlkey=fd8on8x3zhyfdzldl8nw4cdyd&st=k0ntluum&dl=0" alt=""> -->
        <div v-if="getAuth" @mouseover="redraw" class="content" v-masonry="containerId" transition-duration="0.4s" item-selector=".item" stagger="0.03s">
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