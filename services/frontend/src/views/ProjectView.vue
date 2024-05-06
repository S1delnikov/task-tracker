<template>
    <div class="project">
        <div id="project__todo-board" class="project__task-board">
            <div class="title">Ожидают выполнения</div>
            <div class="task-board__task">
                <div class="task__title">Task Title</div>
                <div class="task__description">Lorem ipsum dolor sit amet consectetur adipisicing elit. Animi natus beatae debitis quis ex ab inventore aliquam! Praesentium ab fugiat, eius velit dolorum amet aspernatur harum dolor quam incidunt iste.</div>
                <div class="task__control">
                    <div class="control__btn-to-in-progress">
                        <img src="@/assets/icons/move-one-right-icon.svg" alt="">
                    </div>
                    <div class="control__btn-to-done">
                        <img src="@/assets/icons/move-two-right-icon.svg" alt="">
                    </div>
                </div>
            </div>
        </div>
        <div id="project__in-progress-board" class="project__task-board">
            <div class="title">В процессе</div>
            <div class="task-board__task">
                <div class="task__title">Task Title</div>
                <div class="task__description">Lorem ipsum dolor sit amet consectetur adipisicing elit. Animi natus beatae debitis quis ex ab inventore aliquam! Praesentium ab fugiat, eius velit dolorum amet aspernatur harum dolor quam incidunt iste.</div>
                <div class="task__control">
                    <div class="control__btn to-todo">
                        <img src="@/assets/icons/move-one-left-icon.svg" alt="">
                    </div>
                    <div class="control__btn to-done">
                        <img src="@/assets/icons/move-one-right-icon.svg" alt="">
                    </div>
                </div>
            </div>
        </div>
        <div id="project__done-board" class="project__task-board">
            <div class="title">Выполнены</div>
            <div class="task-board__task">
                <div class="task__title">Task Title</div>
                <div class="task__description">Lorem ipsum dolor sit amet consectetur adipisicing elit. Animi natus beatae debitis quis ex ab inventore aliquam! Praesentium ab fugiat, eius velit dolorum amet aspernatur harum dolor quam incidunt iste.</div>
                <div class="task__control">
                    <div class="control__btn-to-in-progress">
                        <img src="@/assets/icons/move-two-left-icon.svg" alt="">
                    </div>
                    <div class="control__btn-to-done">
                        <img src="@/assets/icons/move-one-left-icon.svg" alt="">
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ProjectView'
}
</script>

<style scoped>
.project {
    display: flex;
    justify-content: space-between;
    margin-top: 4rem;
    /* margin-bottom: 4rem; */
    margin-right: 4rem;
}

.title {
    font-size: 2.4rem;
    padding-top: 1rem;
    padding-bottom: 1rem;
    color: #8EE4AF;
    background-color: #379683;
    text-align: center;
}

/* .test {
    height: 50rem;
    background-color: #fff;
} */

.project__task-board {
    background-color: #8EE4AF;
    width: 30%;
    height: 95vh;
    overflow: scroll;
}

.task-board__task {
    /* height: 10%; */
    background-color: #EDF5E1;
    margin-top: 1rem;
}

.task__title {
    text-align: center;
    font-size: 1.8rem;
    font-weight: 500;
    padding-top: 1rem;
    margin-bottom: 1rem;
}

.task__description {
    display: block;
    padding-left: 0.8rem;
    padding-right: 0.8rem;
    text-align: justify;
    overflow: scroll;
    height: 2rem;
    font-size: 1.4rem;
}

.task__control {
    display: flex;
    justify-content: space-around;
    width: 30%;
    margin: 1rem auto;
}

/* .project__in-progress-board {
    background-color: blue;
    width: 30%;
    height: 95vh;
}

.project__done-board {
    background-color: red;
    width: 30%;
    height: 95vh;
} */
</style>