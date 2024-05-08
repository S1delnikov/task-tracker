<template>
    <div class="container">
        <div v-if="getAuth==true">
            <p>Authenticated!!!!!</p>
            <p>Тут будет профиль</p>
            <button type="button" @click="logoutSubmit">Выйти</button>
        </div>
        <div v-else>
            <form action="" @submit.prevent="loginSubmit" class="login-form">
                <div class="login-form__fields">
                    <label for="uname">Имя пользователя</label>
                    <input class="users-input" v-model="loginForm.login" type="text" name="uname" placeholder="Введите имя пользователя" required>
        
                    <label for="pswd">Пароль</label>
                    <input class="users-input" v-model="loginForm.password" type="password" name="pswd" placeholder="Введите пароль" required>

                    <button class="btn-submit" type="submit">Войти</button>
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
            auth: Boolean = false,
            loginForm: {
                login: '',
                password: ''
            }
        }
    },
    computed: {
        ...mapGetters(['getAuth']),
    },
    methods: {
        ...mapMutations(['logout']),
        ...mapActions(['login', 'checkAuth']),
        changeAuth() {
            if (this.auth==false)
                this.auth = true
            else 
                this.auth = false
            return this.auth
        },
        async loginSubmit() {
            await this.login(this.loginForm)
            // return localStorage.getItem('isAuthenticated')
        },
        async logoutSubmit() {
            await this.logout()
            // await this.logout()
            // return localStorage.getItem('isAuthenticated')
        }
    },
    async mounted() {
        this.checkAuth()
    },
}
</script>

<style scoped>
.container {
    width: 50%;
    margin: 0 auto;
    background-color: #E6ECDC;
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
</style>