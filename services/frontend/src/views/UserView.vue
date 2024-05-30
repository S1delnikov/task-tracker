<template>
    <div class="container">
        <div v-if="getAuth==true">
            <div class="profile">
                <div class="profile__picture">
                    <img :src="getCurrentUser.picture" alt="">
                    <div class="picture__control">
                        <button type="button" @click="openFilePicker">Изменить</button>
                        <button type="button" @click="deleteProfilePic">Удалить</button>
                        <input type="file" id="filePicker" class="hidden" @change="uploadProfilePic" accept="image/*">
                    </div>
                </div>
                <div class="profile__fields">
                    <div class="profile__searchname">
                        <p>Идентификатор:</p>
                        <input type="text" id="searchname" v-model="getCurrentUser.searchname" placeholder="По нему вас будут искать другие пользователи" title="По нему вас будут искать другие пользователи">
                    </div>
                    <div class="profile__full-name">
                        <p>Имя пользователя:</p>
                        <input type="text" id="full-name" v-model="getCurrentUser.full_name" placeholder="Его будет видно другим пользователям" title="Его будет видно другим пользователям">
                    </div>
                    <div class="profile__update-data">
                        <button type="button" @click="tryUpdateUserInfo(getCurrentUser)">Обновить</button>
                    </div>
                    <div class="profile__disabled">
                        <input type="checkbox" v-model="getCurrentUser.disabled" id="disabled">
                        <label class="profile__label" for="disabled">Разрешить добавлять меня в проекты</label>
                    </div>
                </div>
            </div>
            <button class="logout-btn" type="button" @click="logoutSubmit">Выйти</button>
        </div>
        <div v-else>
            <form v-if="hasAccount" @submit.prevent="login(loginForm)" class="login-form">
                <div class="login-form__header">
                    <h2>Авторизация</h2>
                </div>
                <div class="login-form__fields">
                    <label for="uname">Имя пользователя</label>
                    <input class="users-input" v-model="loginForm.login" type="text" name="uname" placeholder="Введите имя пользователя" required>
        
                    <label for="pswd">Пароль</label>
                    <input class="users-input" v-model="loginForm.password" type="password" name="pswd" placeholder="Введите пароль" required>

                    <button class="btn-submit" type="submit">Войти</button>
                    <button @click="switchForm">Зарегистрироваться</button>
                </div>
            </form>
            <form v-else>
                <h2>Регистрация</h2>
            </form>

        </div>
    </div>
</template>

<script>
import { mapActions, mapMutations, mapGetters } from 'vuex'
export default {
    name: 'UserView',
    data() {
        return {
            hasAccount: true,
            loginForm: {
                login: '',
                password: ''
            }
        }
    },
    computed: {
        ...mapGetters(['getAuth', 'getCurrentUser']),
    },
    methods: {
        ...mapMutations(['logout']),
        ...mapActions(['login', 'checkAuth', 'fetchCurrentUser', 'updateUserInfo', 'uploadProfilePic', 'deleteProfilePic']),
        openFilePicker() {
            let filePicker = document.getElementById('filePicker')
            filePicker.click()
        },
        async loginSubmit() {
            await this.login(this.loginForm)
            // return localStorage.getItem('isAuthenticated')
        },
        async logoutSubmit() {
            await this.logout()
            // await this.logout()
            // return localStorage.getItem('isAuthenticated')
        },
        async tryUpdateUserInfo(currentUser) {
            let searchnameInput = document.getElementById('searchname')
            let fullNameInput = document.getElementById('full-name')
            if (searchnameInput.value.length > 32 || searchnameInput.value.length < 5) {
                alert('Длина идентификатора должна быть не меньше 5 и не больше 32 символов.')
                return
            }
            searchnameInput.value = searchnameInput.value.trim()
            if (searchnameInput.value.includes(' ')) {
                alert('Идентификатор не должен содержать пробелов')
                return
            }
            if (fullNameInput.value.length > 128 || fullNameInput.value.length < 1) {
                currentUser.full_name = currentUser.searchname
            }
            this.updateUserInfo(currentUser)
        },
        switchForm() {
            this.hasAccount = !this.hasAccount
        }
    },
    created() {
        this.checkAuth()
    },
    mounted() {
        this.fetchCurrentUser()
    },
}
</script>

<style scoped>
/* @media (max-width: 768px) { */
     
    
.container {
    width: 50%;
    margin: 2rem auto;
    background-color: #E6ECDC;
    border-radius: 2rem;
}

.profile {
    display: flex;
    flex-wrap: wrap;
    /* justify-content: space-between; */
    padding: 2rem;
    width: 100%;
}

.profile__picture {
    width: 50%;
}

.profile__picture img {
    width: 100%;
    display: block;
    padding: auto;
    border-radius: 1.5rem;
}

.picture__control {
    margin-top: 1rem;
    display: flex;
    justify-content: space-between;
}

.picture__control button {
    font-size: 1.6rem;
    padding: 1rem;
    border: none;
    background-color: #379683;
    color: #8EE4AF;
    border-radius: 2rem;
}

.picture__control button:hover {
    background-color: #318675;
}

.profile__fields {
    margin-left: 3rem;
    display: flex;
    flex-direction: column;
    width: 40%;
}

.profile__fields input[text] {
    display: block;
    width: 100%;
}

.profile__searchname {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 100%;
}

.profile__searchname input {
    background-color: #8EE4AF;
    font-size: 1.8rem;
    border: none;
    border-radius: 1rem;
    padding: 1rem;
    margin-top: 0.5rem;
}

.profile__searchname input:focus {
    outline: 0.2rem solid #379583;
}

.profile__full-name {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 100%;
    margin-top: 3rem;
}

.profile__full-name input {
    background-color: #8EE4AF;
    font-size: 1.8rem;
    border: none;
    border-radius: 1rem;
    padding: 1rem;
    margin-top: 0.5rem;
}

.profile__full-name input:focus {
    outline: 0.2rem solid #379583;
}

.profile__full-name p {
    font-size: 1.6rem;
}

.profile__searchname p {
    font-size: 1.6rem;
}

.profile__disabled {
    display: flex;
    align-items: center;
    margin-top: auto;
    margin-bottom: 5rem;
}

.profile__label {
    font-size: 1.2rem;
    margin-left: 2rem;
}

.profile__update-data {
    margin-top: 2rem;
}

.profile__update-data button {
    display: block;
    margin-left: auto;
    margin-right: 0;
    font-size: 1.6rem;
    padding: 1rem 2rem;
    border: none;
    background-color: #379683;
    color: #8EE4AF;
    border-radius: 2rem;
}

.profile__update-data button:hover {
    background-color: #318675;
}

.logout-btn {
    margin-left: 2rem;
    margin-bottom: 1rem;
    padding: 1rem 2.5rem;
    font-size: 1.6rem;
    background-color: #F2BEBE;
    border: none;
    border-radius: 2rem;
}

.logout-btn:hover {
    background-color: #ff9393;
}

.login-form {
    display: block;
    margin: 0 auto;
    /* align-items: center; */
    width: 50%;
}

.login-form__fields {
    display: flex;
    flex-direction: column;
    /* align-items: center; */
}

.users-input {
    width: 100%;
    border-radius: 0.5rem;
    outline: none;
    border: 0.1rem solid #000;
    padding: 1rem;
    font-size: 1.6rem;
}

.btn-submit {
    width: 20%;
    font-size: 1.6rem;
    margin-top: 3rem;
    margin-left: auto;
    margin-right: auto;
    padding: 0.7rem;
    border-radius: 0.4rem;
    border: none;
    background-color: #379683;
    color: #8EE4AF;
}


label {
    font-size: 2rem;
    margin-top: 2rem;
    margin-bottom: 1rem;
}

input::placeholder {
    font-size: 1.2rem;
    text-overflow: ellipsis;
}

.hidden {
    opacity: 0;
    height: 0;
    width: 0;
    line-height: 0;
    overflow: hidden;
    padding: 0;
    margin: 0;
}
/* } */
</style>