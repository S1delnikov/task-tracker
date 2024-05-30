<template>
    <div class="dialog" v-if="show" @click="hideDialog">
        <div @click.stop class="dialog__content">
            <slot></slot>
        </div>
    </div>
</template>

<script>
export default {
    name: 'DialogView',
    props: {
        show: {
            type: Boolean,
            default: false
        }
    },
    methods: {
        hideDialog() {
            this.$emit('update:show', false)
        }
    }
}
</script>

<style scoped>
.dialog {
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
    background: rgba(0, 0, 0, 0.5);
    position: fixed;
    z-index: 1;
    display: flex;
}

.dialog__content {
    margin: auto;
    padding: 1rem;
    background-color: #EDF5E1;
    border-radius: 1.2rem;
    height: fit-content;
    /* width: 50%; */
    width: fit-content;
}
</style>