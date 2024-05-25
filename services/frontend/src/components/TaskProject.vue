<template>
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
</template>

<script>
export default {
    name: 'TaskProject',
    props: {
        task: Object,
        required: true
    }
}
</script>

<style>
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
</style>