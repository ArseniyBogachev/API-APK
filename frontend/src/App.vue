<template>
  <div class="app">
    <div class="content container-md">
      <div class="row">
        <NavBar class="col-3"></NavBar>
        <router-view class="col-9"></router-view>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar";
export default {
  name: "App",
  components:{
    NavBar,
  }
}
</script>

<style scoped>
  .app{
    background-color: #0c8558;
    width: 100vw;
    height: 100vh;
    padding-top: 15vh;
  }
  .content{
    background-color: white;
    width: 100vw;
    height: 85vh;
  }
  .nav-bar{
    width: 100%;
    height: 100%;
    background-color: #403a39;
  }
</style>
