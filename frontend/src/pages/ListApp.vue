<template>
  <div class="main">
    <div class="wrapper">
      <h5 class="title">POSSIBLE HARDCODED SECRETS</h5>
      <ul class="list" v-for="k in keys" v-if="keys">
        <li>{{k}}</li>
      </ul>
      <span class="miss" v-else>Choice application</span>
    </div>
    <div class="input-group input-group-sm mb-3">
      <span class="input-group-text" id="inputGroup-sizing-sm">Search application</span>
      <input type="text" class="form-control" aria-label="Пример размера поля ввода" aria-describedby="inputGroup-sizing-sm">
    </div>
    <div class="list-group" id="element">
      <button
          type="button"
          class="list-group-item list-group-item-action"
          v-bind:class="{'list-group-item-success': app.active, 'active': app.active}"
          aria-current="true"
          v-for="app in application"
          v-on:click="class_active(app)"
      >
        {{app.title}}
      </button>
    </div>
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex';
export default {
  name: "ListApp",
  data(){
    return{
      keys: null,
    }
  },
  methods:{
    ...mapActions({
      get_keys: 'get_keys',
    }),
    class_active(app){
      for (let i of this.application){
        i.active = false
      }
      app.active = true
      this.keys = app.api_keys
    }
  },
  computed:{
    ...mapGetters({
      application: 'application',
    }),
  },
  created() {
    this.get_keys()
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
  .list-group{
    margin-top: 20px;
    height: 400px;
    overflow-y: scroll;
    box-shadow: 0 0 5px 1px #a4a0a2;
    background-color: #edf7ed;
  }
  #element::-webkit-scrollbar {
    width: 7px;
    background-color: white;
    border-radius: 10px;
  }
  #element::-webkit-scrollbar-thumb {
    background-color: #474345;
    border-radius: 10px;
  }
  .input-group{
    margin-top: 20px;
    width: 350px;
  }
  .list{
    list-style-type: none;
  }
</style>