<template>
    <div class="checklist">
        <div class="checklist__body">
            <div class="checklist__control">
                <div class="control__edit" type="button"><img src="@/assets/icons/edit-icon.webp" alt="Edit"></div>
                <button class="control__cross-mark" type="button" @click="deleteTask(task)"><img src="@/assets/icons/cross-mark-icon.webp" alt=""></button>
            </div>
            <div class="checklist__title">
                <input type="text" class="title" v-model="task.title" @change="updateTask(task)"></input>
            </div>
            <div class="checklist__main">
                <div class="checklist__todo" v-for="subtask in task.subtasks" :key="subtask.id_subtask">
                    <label class="todo__checkbox">
                        <input class="todo__real-checkbox" type="checkbox" v-model="subtask.done">
                        <span class="todo__custom-checkbox"></span>
                    </label>
                    <input class="todo__text" type="text" v-model="subtask.description">
                    <!-- <p>{{ task }}</p> -->
                    <button class="todo__update" type="button" @click="updateSubtask(subtask)"><img src="@/assets/icons/refresh-icon.webp" alt="Обновить"></button>
                    <button class="todo__delete" type="button" @click="deleteSubtask(subtask)"><img src="@/assets/icons/delete-icon_2.webp" alt="Удалить"></button>
                </div>
            </div>
            <div class="checklist__add-todo">
                <button class="add-todo" type="button" @click="createSubtask(task)">
                    <img src="@/assets/icons/plus-icon.webp" alt="Добавить">
                </button>
            </div>
        </div>
    </div>
</template>

<script>
import { mapMutations, mapActions} from 'vuex'
export default {
    name: 'Checklist',
    props: {
        task: {
            type: Object,
            required: true
        }
    },
    methods: {
        ...mapMutations(['setTaskTitle']),
        ...mapActions(['updateTask', 'deleteTask', 'createSubtask', 'updateSubtask', 'deleteSubtask']),
        testEmit() {
            this.$emit('test', this.task)
            // console.log(this.task)

        },
        flashback() {
            console.log('boom')
        }
    }
}
</script>

<style scoped>
.checklist{
    background-color: #EDF5E1;
    width: 25%;
    border-radius: 3rem;
}

.checklist__body {
    margin: 2rem;
    /* background-color: aqua; */
}

.checklist__control {
    display: flex;
    justify-content: space-between;
    padding-top : 0.4rem;
    margin-bottom: 1rem;
}

.control__edit {
    background-color: #EDF5E1;
    border: none;
}

.control__cross-mark {
    background-color: #F95E5E;
    border: none;
}

.control__cross-mark:hover {
    background-color: #e95757;
}

.checklist__title {
    margin-bottom: 1rem;
}

.title {
    display: block;
    margin: 0 auto;
    font-size: 2.5rem;
    text-align: center;
    background-color: #E6ECDC;
    border: none;
    width: 90%;
    color: #000;
}

.title:focus {
    outline: 0.1rem solid #ccd1c5;
}

.checklist__todo {
    display: flex;
    justify-content: space-between;
    margin-bottom: 1rem;
    align-items: center;
}

.todo__checkbox {
    padding-right: 1rem;
}

.todo__real-checkbox {
    width: 0;
    height: 0;
    opacity: 0;
    position: absolute;
    z-index: -1;
}

.todo__custom-checkbox {
    position: relative;
    display: inline-block;
    width: 3.2rem;
    height: 3.2rem;
    background-color: #fff;
    border: 0.1rem solid #000;
}

.todo__custom-checkbox::before {
    content: '';
    display: inline-block;
    width: 1.3rem;
    height: 1.3rem;
    background-image: url('@/assets/icons/complete-icon.svg');
    background-size: contain;
    background-repeat: no-repeat;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%) scale(0);
    margin-top: 0.1rem;

    transition: 0.2s ease-in;
}

.todo__real-checkbox:checked + .todo__custom-checkbox::before {
    transform: translate(-50%, -50%) scale(2);
    background-color: #C0F9A5;
}

.todo__real-checkbox:checked + .todo__custom-checkbox {
    background-color: #C0F9A5;
}

.todo__text {
    width: 70%;
    border-radius: 0.5rem;
    outline: none;
    border: 0.1rem solid #000;
    padding: 1rem;
    font-size: 1.6rem;
}

.todo__update {
    background-color: #90F95E;
    border: none;
}

.todo__update:hover {
    background-color: #82e455;
}

.todo__delete {
    background-color: #FD7070;
    border: none;
}

.todo__delete:hover {
    background-color: #e66767;
}

.add-todo {
    background-color: #5DE192;
    border: none;
}

.add-todo:hover {
    background-color: #51c47f;
}

@media (max-width: 1600px) {
    .checklist {
        width: 30rem;
    }

    .checklist__body {
        margin: 1rem;
    }

    .title {
        width: 95%;
        font-size: 2rem;
    }

    .todo__custom-checkbox  {
        width: 2.5rem;
        height: 2.5rem;
    }

    .todo__custom-checkbox::before {
        width: 1.3rem;
        height: 1.3rem;
    }

    .todo__real-checkbox:checked + .todo__custom-checkbox::before {
        transform: translate(-50%, -50%) scale(1.5);
        background-color: #C0F9A5;
    }

    .todo__text {
        font-size: 1.6rem;
        padding: 0.4rem;
    }

    .todo__update img{
        width: 2.8rem;
    }

    .todo__delete img{
        width: 2.8rem;
    } 
}

@media (max-width: 1280px) {
    /* .checklist {
        margin: 1rem;
    } */

    .checklist {
        width: 45%;
    }

    .checklist__body {
        margin: 1rem;
    }

    .title {
        width: 95%;
        font-size: 2rem;
    }

    .todo__custom-checkbox  {
        width: 2.5rem;
        height: 2.5rem;
    }

    .todo__custom-checkbox::before {
        width: 1.3rem;
        height: 1.3rem;
    }

    .todo__real-checkbox:checked + .todo__custom-checkbox::before {
        transform: translate(-50%, -50%) scale(1.5);
        background-color: #C0F9A5;
    }

    .todo__text {
        font-size: 1.6rem;
        padding: 0.4rem;
    }

    .todo__update img{
        width: 2.8rem;
    }

    .todo__delete img{
        width: 2.8rem;
    }
}

@media (max-width: 1024px) {
    .checklist {
        width: 30rem;
    }

    .checklist__body {
        margin: 1rem;
    }

    .title {
        width: 95%;
        font-size: 1.8rem;
    }

    .todo__custom-checkbox  {
        width: 2.8rem;
        height: 2.8rem;
    }

    .todo__custom-checkbox::before {
        width: 1.3rem;
        height: 1.3rem;
    }

    .todo__real-checkbox:checked + .todo__custom-checkbox::before {
        transform: translate(-50%, -50%) scale(1.5);
        background-color: #C0F9A5;
    }

    .todo__text {
        font-size: 1.4rem;
        padding: 0.4rem;
    }

    .todo__update img{
        width: 2.2rem;
    }

    .todo__delete img{
        width: 2.2rem;
    }
}

@media (max-width: 768px) {
    .checklist {
        width: 30rem;
    }

    .checklist__body {
        margin: 1rem;
    }

    .title {
        width: 95%;
        font-size: 1.8rem;
    }

    .todo__custom-checkbox  {
        width: 2.5rem;
        height: 2.5rem;
    }

    .todo__custom-checkbox::before {
        width: 1.3rem;
        height: 1.3rem;
    }

    .todo__real-checkbox:checked + .todo__custom-checkbox::before {
        transform: translate(-50%, -50%) scale(1.5);
        background-color: #C0F9A5;
    }

    .todo__text {
        font-size: 1.4rem;
        padding: 0.4rem;
    }

    .todo__update img{
        width: 2.2rem;
    }

    .todo__delete img{
        width: 2.2rem;
    }
}
</style>