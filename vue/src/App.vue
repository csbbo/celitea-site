<template>
  <div id="app"> 
    <nav-bar></nav-bar>
    <main>
      <aside-part></aside-part>
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
import NavBar from './components/navbar.vue'
import Aside from './components/aside.vue'

export default {
  name: 'app',
  components:{ 
    'nav-bar':NavBar,
    'aside-part':Aside
  }
}
</script>

<style>
</style>
