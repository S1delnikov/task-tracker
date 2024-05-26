<template>
    <div class="dialog">
        <div class="dialog__content">
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
    background-color: #fff;
    border-radius: 1.2rem;
    min-height: 5rem;
    min-width: 30rem;
}
</style>