<template>
    <div class="menu-item">
        <div class="menu-item__preview">
            <img class="preview" src="@/assets/antarctica3.jpg" alt="Изображение проекта">
        </div>
        <div class="menu-item__name">
            <h2 class="name">Project name</h2>
        </div>
        <div class="menu-item__description">
            <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Deserunt hic aperiam dolor blanditiis, rem perspiciatis officia itaque necessitatibus laudantium magni iusto praesentium quod quo dolore distinctio optio quisquam. Atque nisi voluptatem quidem, possimus numquam hic reiciendis iusto libero at beatae voluptate repellendus voluptates rem cupiditate repudiandae? Quia pariatur illo distinctio similique cum, assumenda modi ipsa, consectetur esse nihil natus fuga? Harum molestias tempore consequatur quas ea a numquam necessitatibus aliquam molestiae aspernatur temporibus itaque repudiandae odit autem ipsum soluta possimus maxime, qui dolor inventore vel delectus! Accusantium veniam doloremque maxime accusamus excepturi laudantium maiores distinctio? Perspiciatis fuga velit dolores aspernatur!. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus vero possimus nobis quisquam harum, laboriosam voluptas quam quasi provident ipsum.</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ProjectMenuItem'
}
</script>

<style scoped>
.menu-item {
    background-color: #EDF5E1;
    width: 35%;
    padding: 2rem;
    border-radius: 3rem;
}

.menu-item__preview {
    width: fit-content;
    overflow: hidden;
    display: block;
    margin: 0 auto;
    background-color: antiquewhite;
}

.preview {
    width: 40rem;
    border: 0.1rem solid #000;
}

.menu-item__name {
    display: block;
    margin: 0 auto;
    margin-top: 0.5rem;
    margin-bottom: 1.5rem;
    text-align: center;
}

.name {
    font-size: 2.6rem;
    text-wrap: nowrap;
    overflow: scroll;
    text-overflow: ellipsis;
}

.menu-item__description {
    display: block;
    margin: 0 auto;
}
</style>