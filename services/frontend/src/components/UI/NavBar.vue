<template>
    <nav id="sidebar" class="sidebar">
        <div class="user">
            <div class="user__picture" @click="$router.push('/')">
                <img v-if="getCurrentUser" :src="getCurrentUser.picture" alt="Profile picture" class="user__picture">
                <img v-else src="@/assets/icons/profile_pic.jpeg" class="user__picture" alt="Profile picture">
            </div>
            <div class="user__username" :title="getCurrentUser.searchname">{{ getCurrentUser.searchname }}</div>
        </div>
        <div class="sidebar__btns">
            <div class="sidebar__btn">
                <button class="route-btn" @click="$router.push('/')">
                    <img src="@/assets/icons/menu-profile-icon.webp" alt="">   
                    Профиль</button>
            </div>
            <div class="sidebar__btn">
                <button @click="submenu" class="dropdown-btn">
                    <img src="@/assets/icons/tasks-icon.webp" alt="">   
                    Задачи</button>
                    <div class="dropdown-container">
                        <router-link class="dropdown-container__links" to="/checklists">Чеклисты</router-link>
                        <router-link class="dropdown-container__links" to="/projects_menu">Проекты</router-link>
                    </div>
            </div>
            <div class="sidebar__btn">
                <button class="route-btn" @click="$router.push('/documents')">
                    <img src="@/assets/icons/doc-icon.webp" alt="">   
                    Документы</button>
            </div>
        </div>
    </nav>
    <div class="toggleSidebarBtn">
        <button id="toggleSidebarBtn" type="button" @click="openSidebar"><img style="transition: 2.5s;" :src="sidebarBtnImage" alt="Меню"></button>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
    data: () => ({
        opened: false,
        sidebarBtnImage: require('@/assets/icons/open-sidebar-icon.svg')
    }),
    name: 'NavBar',
    computed: {
        ...mapGetters(['getCurrentUser'])
    },
    methods: {
        submenu() {
            let element = document.getElementsByClassName("dropdown-container")
            if (element[0].style.display == 'block')
                element[0].style.display = 'none'
            else 
                element[0].style.display = 'block'
        },
        openSidebar() {
            let toggleSidebarBtnBlock = document.getElementsByClassName('toggleSidebarBtn')[0]
            let toggleSidebarBtn = document.getElementById('toggleSidebarBtn')
            let sidebar = document.getElementById('sidebar')

            if (!this.opened) {
                sidebar.style.width = '25rem'
                this.opened = true
                toggleSidebarBtn.firstChild.src = require('@/assets/icons/close-sidebar-icon.svg')
                toggleSidebarBtnBlock.style.left = `21.8rem`
                console.log(toggleSidebarBtnBlock.style.left)
            }
            else {
                sidebar.style.width = '0rem'
                this.opened = false
                toggleSidebarBtn.firstChild.src = require('@/assets/icons/open-sidebar-icon.svg')
                toggleSidebarBtnBlock.style.left = `0`
            }
        },
    }
}
</script>

<style scoped>
.sidebar {
  height: 100%;
  width: 22rem;
  position: fixed;
  z-index: 9999;
  top: 0;
  left: 0;
  background-color: #05386B;
  overflow-x: hidden;
  padding-top: 16px;
  transition: 0.5s;
}

/* Style sidebar links */
.sidebar a, .route-btn, .dropdown-btn {
  padding: 6px 8px 6px 16px;
  text-decoration: none;
  font-size: 20px;
  background-color: #379683;
  border: none;
  color: #8EE4AF;
  width: 100%;
  display: block;   
}

/* Style links on mouse-over */
.sidebar a:hover, .route-btn:hover, .dropdown-btn:hover {
  color: #f1f1f1;
}

/* Add media queries for small screens (when the height of the screen is less than 450px, add a smaller padding and font-size) */
/* @media screen and (max-height: 450px) {
  .sidebar {padding-top: 15px;}
  .sidebar a {font-size: 18px;}
} */

.dropdown-btn {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-radius: 0.4rem 0.4rem 0rem 0.4rem; 
    height: 5.8rem;
}

.route-btn {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-radius: 0.4rem; 
    height: 5.8rem;
}

.active {
  background-color: green;
  color: white;
}

.dropdown-container {
    display: none;
    padding-left: 2rem;
    padding-bottom: 2rem;
}

.dropdown-container__links {
    outline: 1px solid #05386B;
}

.sidebar__btns {
    margin-top: 8rem;
    align-items: center;
    width: 100%;
    height: 25rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.sidebar__btn {
    width: 90%;
    margin-bottom: 4rem;
}

.user {
    margin-left: 0.4rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    /* background-color: aliceblue ; */
}

.user__picture {
    width: 7.8rem;
    height: 7.8rem;
    border-radius: 50%;
}

.user__picture:hover {
    cursor: pointer;
}

.user__username {
    font-size: 1.6rem;
    padding-left: 1rem;
    overflow: hidden;
    text-overflow: ellipsis;
    color: #fff;
    display: block;
    margin: auto;
}

.toggleSidebarBtn {
    display: none;
}

@media (max-width: 1280px) {
    .sidebar {
        width: 20rem;
    }
}

@media (max-width: 1024px) {
    .sidebar {
        width: 15rem;
    }

    .route-btn, .dropdown-btn, .sidebar a {
        font-size: 1.4rem;
    }
}

@media  (max-width: 768px){
    .sidebar {
        width: 0;
    }

    .toggleSidebarBtn {
        display: block;
        position: fixed;
        left: 0;
        bottom: 0;
        z-index: 9999;
        transition: 0.5s;
    }

    #toggleSidebarBtn {
        background-color: rgba(0, 0, 0, 0);
        border: none;

    }

    #toggleSidebarBtn > img{
    display: block;
    padding: auto;
    }
}
</style>