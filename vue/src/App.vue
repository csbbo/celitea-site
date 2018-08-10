<template>
  <div id="app"> 
    <nav-bar></nav-bar>
    <main>
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
import NavBar from './components/navbar.vue'

export default {
  name: 'app',
  components:{ 
    'nav-bar':NavBar,
  }
}
</script>

<style>
@media screen and (max-width:600px) {
  .self-com{
   width: 80%;
   margin: 0 10%
 }
}

@media screen and (min-width: 601px){
  .self-com{
    width:60%;
    margin: 0 20%
  }
}
 
</style>
