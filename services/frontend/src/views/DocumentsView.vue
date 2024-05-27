<template>
    <div class="documents">
        <div class="documents__control">
            <button type="button">Загрузить документ</button>
        </div>
        <div class="documents__board">
            <div class="documets__list">
                <div class="document">
                    <input type="text">
                    <button type="button">Управление</button>
                    <button type="button">Скачать</button>
                </div>
                <div class="document">
                    <input type="text">
                    <button type="button">Управление</button>
                    <button type="button">Скачать</button>
                </div>
                <div class="document">
                    <input type="text">
                    <button type="button">Управление</button>
                    <button type="button">Скачать</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'DocumentsView'
}
</script>

<style>
.documents__control {
    margin: 2rem;
}

.documents__control button {
    font-size: 1.6rem;
    padding: 1.5rem;
    border: none;
    background-color: #379683;
    color: #8EE4AF;
    border-radius: 4rem;
    margin: 1rem auto;
    margin-bottom: 0;
    margin-left: 1rem;
}

.documents__control button:hover {
    background-color: #318675;
}

.documents__control button {
    padding: 1rem;
    font-size: 1.8rem;
}

.documents__board {
    background-color: #EDF5E1;
    border-radius: 2rem;
    width: 65%;
    padding: 2rem 4rem;
    margin-left: 12%;
}

.documets__list {
    padding: 2rem;
}

.document {
    padding: 0.4rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
    background-color: #379683;
    border-radius: 1rem;
}

.document input {
    width: 70%;
    font-size: 2.4rem;
    padding: 1rem;
    margin: 0.4rem;
    background-color: #379683;
    border: 0.1rem solid #8EE4AF;
    border-radius: 1rem;
    color: #8EE4AF;
}

.document input:focus {
    outline: 0.1rem solid #8EE4AF
}

.document button {
    width: auto;
    font-size: 1.8rem;
    padding: 0.5rem 1rem;
    background-color: #379683;
    color: #8EE4AF;
    border: none;
}

.document button:hover {
    outline: 0.1rem solid #8EE4AF;
    border-radius: 1rem;
}
</style>