<template>
    <div class="container">
        <div v-if="getAuth">
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
                        <p v-if="getCurrentUser" class="input-counter">{{ getCurrentUser.searchname.length }}/32</p>
                    </div>
                    <div class="profile__full-name">
                        <p>Имя пользователя:</p>
                        <input type="text" id="full-name" v-model="getCurrentUser.full_name" placeholder="Его будет видно другим пользователям" title="Его будет видно другим пользователям">
                        <p v-if="getCurrentUser" class="input-counter">{{ getCurrentUser.full_name.length }}/128</p>
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
            <div class="profile__control">
                <button class="profile__logout-btn" type="button" @click="logoutSubmit">Выйти</button>
                <button class="profile__logout-btn" type="button" @click="confirmDelete">Удалить аккаунт</button>
            </div>
        </div>
        <div v-else>
            <form v-show="hasAccount==true" @submit.prevent="login(form)" class="form">
                <div class="form__header">
                    <h2>Авторизация</h2>
                </div>
                <div class="form__fields">
                    <label for="uname">Имя пользователя</label>
                    <input class="users-input" v-model="form.login" type="text" name="uname" placeholder="Введите имя пользователя" required>
        
                    <label for="pswd">Пароль</label>
                    <input class="users-input" v-model="form.password" type="password" name="pswd" placeholder="Введите пароль" required>

                    <button class="btn-submit" id="signIn-btn" type="submit">Войти</button>
                    <button class="btn-submit" @click="switchForm">Создать аккаунт</button>
                </div>
            </form>
            <form v-show="hasAccount==false" @submit.prevent="tryRegister" class="form">
                <div class="form__header">
                    <h2>Регистрация</h2>
                </div>
                <div class="form__fields">
                    <label for="uname">Логин</label>
                    <input class="users-input" id="regUsername" v-model="form.login" type="text" name="uname" placeholder="Придумайте имя пользователя" required>
                    
                    <label for="pswd">Пароль</label>
                    <input class="users-input" id="regPassword" v-model="form.password" type="password" name="pswd" placeholder="Придумайте пароль" required>

                    <label for="pswdClone">Повторите пароль</label>
                    <input class="users-input" id="regRepeatPassword" v-model="passwordClone" type="password" name="pswdClone" placeholder="Повторите пароль" required>

                    <button class="btn-submit" type="submit">Зарегистрироваться</button>
                    <button class="btn-submit" @click="switchForm">Уже есть аккаунт</button>
                </div>
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
            form: {
                login: '',
                password: ''
            },
            passwordClone: '',
        }
    },
    computed: {
        ...mapGetters(['getAuth', 'getCurrentUser']),
    },
    methods: {
        ...mapMutations(['logout']),
        ...mapActions(['register', 'login', 'checkAuth', 'fetchCurrentUser', 'updateUserInfo', 'uploadProfilePic', 'deleteProfilePic', 'deleteProfile']),
        openFilePicker() {
            let filePicker = document.getElementById('filePicker')
            filePicker.click()
        },
        async tryRegister() {
            let regUsername = document.getElementById('regUsername')
            let regPassword = document.getElementById('regPassword')
            let regRepeatPassword = document.getElementById('regRepeatPassword')
            if (regUsername.value.length > 64 || regUsername.value.length < 5) {
                alert('Длина логина должна быть от 5 до 64 символов без пробелов.')
                return
            }
            regUsername.value = regUsername.value.trim()
            if (regUsername.value.includes(' ')) {
                alert('Логин не должен содержать пробелов')
                return
            }
            if (regPassword.value.length < 9) {
                alert('Минимальная длина пароля составляет 9 символов без пробелов')
                return
            }
            regPassword.value = regPassword.value.trim()
            if (regPassword.value.includes(' ')) {
                alert('Пароль не должен содержать пробелов')
                return
            }
            if (regPassword.value != regRepeatPassword.value) {
                alert('Пароли не совпадают.')
                return
            }
            this.register(this.form)
        },
        async logoutSubmit() {
            await this.logout()
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
            if (fullNameInput.value.length > 128) {
                alert('Длина имени пользователя должна быть не меньше 1 и не больше 128 символов.')
                return
            }
            if (fullNameInput.value.length < 1) {
                currentUser.full_name = currentUser.searchname
            }
            this.updateUserInfo(currentUser)
        },
        async confirmDelete() {
            let paracetomol = 'ПАРАЦЕТОМОЛ'
            let input = prompt(`Для удаления проекта введите слово ${paracetomol}.`, '');
            if (input != paracetomol && input != null) {
                alert('Ошибка удаления. Попробуйте снова.')
            }
            else if (input==paracetomol) {
                await this.deleteProfile()
            }
        },
        switchForm() {
            this.hasAccount = !this.hasAccount
        }
    },
    created() {
        // this.checkAuth()
        this.fetchCurrentUser()
    },
    mounted() {
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
    overflow-x: scroll;
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
    width: 12rem;
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

.input-counter {
    padding-top: 0.4rem;
    
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

.profile__control {
    display: flex;
    justify-content: space-between;
    padding-right: 2rem;
    /* background-color: #fff; */
}

.profile__logout-btn {
    margin-left: 2rem;
    margin-bottom: 1rem;
    padding: 1rem 2.5rem;
    font-size: 1.6rem;
    background-color: #F2BEBE;
    border: none;
    border-radius: 2rem;
}

.profile__logout-btn:hover {
    background-color: #ff9393;
}

.form {
    display: block;
    margin: 0 auto;
    width: 50%;
    /* padding: 2rem; */
}

.form__header {
    padding-top: 1rem;
}

.form__header h2 {
    font-size: 2.2rem;
}

.form__fields {
    display: flex;
    flex-direction: column;
    padding-bottom: 1rem;
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
    /* width: fit-content; */
    width: 18.5rem;
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

.btn-submit:hover {
    background-color: #318675;
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
    position: fixed;
    z-index: -999;
}

@media (max-width: 1600px) {
    .container {
        width: 85rem;
        margin-top: 0.5rem;
    }

    .profile__fields {
        width: 37rem;
    }
}

@media (max-width: 1280px) {
    .container {
        width: 70rem;
    }

    .profile__fields {
        width: 30rem;
    }

    .profile__logout-btn {
        width: 20rem;
    }
}

@media  (max-width: 1024px) {
    .container {
        width: 60rem;
    }

    .form {
        width: 95%;
    }

    .profile__fields {
        width: 25rem;
    }
}

@media  (max-width: 768px){
    .container {
        width: 30.4rem;
    }
    .form {
        width: 95%;
    }
    
    .profile {
        padding: 1rem;
    }

    .profile__picture {
        width: 90%;
        margin: auto;
    }

    .picture__control > button{
        width: 10rem;
    }

    .profile__fields {
        width: 90%;
        margin: auto;
        margin-top: 2rem;
    }

    .profile__full-name {
        margin-top: 1rem;
    }

    .profile__update-data {
        margin-top: 0rem;
    }

    .profile__disabled {
        margin-bottom: 0rem;
    }
}
</style>