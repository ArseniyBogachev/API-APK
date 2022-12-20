<template>
  <div class="main">
    <div class="wrapper">
      <h5 class="title">POSSIBLE HARDCODED SECRETS</h5>
      <ul class="list" v-for="k in api_keys" v-if="api_keys.length">
        <li>{{k}}</li>
      </ul>
      <span v-else class="miss">Keys missing</span>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
export default {
  name: "ApiApp",
  computed:{
    ...mapGetters({
      api_keys: 'api_keys',
    }),
  }
}
</script>

<style scoped>
  .main{
    background-color: #ded8d7;
  }
  .wrapper{
    margin-top: 20px;
    background-color: white;
    padding: 2%;
    box-shadow: 0 0 5px 1px #a4a0a2;
    min-height: 270px;
    position: relative;
  }
  .miss{
    font-style: italic;
    color: #807c7e;
    position: absolute;
    top: 50%;
    left: 50%;
    margin-right: -50%;
    transform: translate(-50%, -50%)
  }
  .title{
  }
  .list{
    list-style-type: none;
  }
</style>