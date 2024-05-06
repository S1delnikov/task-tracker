<template>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <nav class="sidebar">
        <div class="user">
            <div class="user__picture">
                <img src="@/assets/pepe.jpeg" alt="Profile picture" class="user__picture">
            </div>
            <div class="user__username">Pepe The Frog</div>
        </div>
        <div class="sidebar__btns">
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
                <button class="route-btn" @click="$router.push('/')">
                    <img src="@/assets/icons/doc-icon.webp" alt="">   
                    Документы</button>
            </div>
            <div class="sidebar__btn">
                <button class="route-btn" @click="$router.push('/')">
                    <img src="@/assets/icons/chat-icon.webp" alt="">   
                    Чаты</button>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    name: 'NavBar',
    methods: {
        submenu() {
            let element = document.getElementsByClassName("dropdown-container")
            if (element[0].style.display == 'block')
                element[0].style.display = 'none'
            else 
                element[0].style.display = 'block'
        },
    }
}
</script>

<style scoped>
.sidebar {
  height: 100%;
  width: 22rem;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  background-color: #05386B;
  overflow-x: hidden;
  padding-top: 16px;
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
@media screen and (max-height: 450px) {
  .sidebar {padding-top: 15px;}
  .sidebar a {font-size: 18px;}
}

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

.user__username {
    font-size: 1.6rem;
    padding-left: 1rem;
    overflow: hidden;
    text-overflow: ellipsis;
    color: #fff;
}
</style>