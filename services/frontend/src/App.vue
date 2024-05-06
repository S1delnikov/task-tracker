<template>
  <NavBar></NavBar>
  <!-- <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav> -->
  <div class="main">
    <!-- <h1>Not view</h1> -->
    <router-view/>
  </div>
</template>

<script>
export default {

}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-size: 10px;
}

.main {
  margin-left: 25rem; /* 22 */
}
</style>
