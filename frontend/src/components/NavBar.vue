<template>
  <div class="wrapper">
    <nav class="nav flex-column">
      <a class="nav-link elem" v-bind:style="upload" href="#" @click.prevent="$router.push('/'); func_upload()">
        <span>Upload file</span>
      </a>
      <a class="nav-link elem" v-bind:style="components" href="#" @click.prevent="$router.push('/api'); func_components()">
        <span>Components</span>
      </a>
    </nav>
  </div>
</template>

<script>
import router from '@/router';
export default {
  name: "NavBar",
  data(){
    return{
      upload: {
        'border': '1px solid white',
        'color': '#1e1a1c',
        'background-color': '#807c7e',
      },
      components: {},
    }
  },
  methods:{
    func_upload(){
      this.upload = {
        'border': '1px solid white',
        'color': '#1e1a1c',
        'background-color': '#807c7e',
      }
      this.components = {}
    },
    func_components(){
      this.components = {
        'border': '1px solid white',
        'color': '#1e1a1c',
        'background-color': '#807c7e',
      }
      this.upload = {}
    },
  },
  created() {
    router.push('/')
  }
}
</script>

<style scoped>
  .wrapper{
    background-color: #474345;
    height: 85vh;
  }
  .elem{
    text-align: center;
    color: white;
    margin-top: 10px;
    border: 1px solid #474345;
    border-radius: 10px;
  }
  .elem:hover{
    border: 1px solid white;
    color: #1e1a1c;
    background-color: #807c7e;
  }
  .elem:active{
    box-shadow: 0 0 2px 1px black inset;
    color: white;
  }
  .elem:focus{
    color: white;
  }
</style>