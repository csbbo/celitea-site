<template>
  <div id="app">
    <el-container>
    <el-header>
      <header-mnue></header-mnue>
    </el-header>
    <el-container>
        <el-main>
            <router-view/>
        </el-main>
    </el-container>
    </el-container>
  </div>
</template>

<script>
import headermnue from './page/login_status'


export default {
  name: 'App',
  components:{
    'header-mnue':headermnue,
  }
}
</script>

<style>

</style>


