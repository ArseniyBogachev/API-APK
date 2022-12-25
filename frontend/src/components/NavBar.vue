<template>
  <div class="wrapper">
    <nav class="nav flex-column">
      <a class="nav-link elem" v-bind:style="choice.upload" href="#" @click.prevent="$router.push('/'); choice_func('upload')">
        <span>Upload file</span>
      </a>
      <a class="nav-link elem" v-bind:style="choice.components" href="#" @click.prevent="$router.push('/api'); choice_func('components')">
        <span>Components</span>
      </a>
      <a class="nav-link elem" v-bind:style="choice.list" href="#" @click.prevent="$router.push('/list'); choice_func('list')">
        <span>List application</span>
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
      choice: {
        upload: {
          'border': '1px solid white',
          'color': '#1e1a1c',
          'background-color': '#807c7e',
        },
        components: {},
        list: {},
      },
    }
  },
  methods:{
    choice_func(style){
      for (let i in this.choice){
        if (style === i){
          this.choice[i] = {
            'border': '1px solid white',
            'color': '#1e1a1c',
            'background-color': '#807c7e',
          }
        }
        else{
          this.choice[i] = {}
        }
      }
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