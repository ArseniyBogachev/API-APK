<template>
  <div>
    <div class="image-upload-wrap">
      <input type="file" class="file-upload-input" @input="file_fn($event)">
      <span v-if="upload_file" class="text">{{ upload_text }}</span>
      <span v-else class="text">Drag files here or click Upload & Analyze</span>
    </div>
    <button type="button" class="btn btn-light"
            v-if="buttonActive"
            v-on:click="post_file(this.upload_file); preloader_func()">
      <span class="style-text">Analyze file</span>
    </button>
    <div class="loading-wrapper" v-else>
      <div class="process_loading" v-if="completeActive">
        <span class="preloader">{{ preloader_text }}</span>
        <div class="progress">
          <div class="progress-bar progress-bar-striped bg-success progress-bar-animated" role="progressbar" v-bind:style="`width: ${loading}%`" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
            {{ loading }}%
          </div>
        </div>
      </div>
      <div class="complete-loading" v-else>
        <span class="text-complete">Complete</span>
        <font-awesome-icon icon="fa-solid fa-check" class="icon-complete"></font-awesome-icon>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
export default {
  name: "HomeApp",
  data(){
    return {
      upload_file: '',
      upload_text: '',
      preloader_text: 'Analyzing',
    }
  },
  methods:{
    ...mapActions({
      post_file: 'post_file',
      startWebSocket: 'startWebSocket',
    }),
    file_fn(e){
      this.upload_file = e.target.files[0]
      this.upload_text = e.target.value.split('\\')[2].length > 40 ? e.target.value.split('\\')[2].slice(0,40) + '...' : e.target.value.split('\\')[2]
    },
    preloader_func(){
      this.preloader_text = 'Analyzing'
      if (!this.buttonActive){
        let interval = setInterval(() => {
          this.preloader_text += '.'
        }, 1000)
        setTimeout(() => {
          clearInterval(interval);
          this.preloader_func()
        }, 4000)
      }
    }
  },
  computed:{
    ...mapGetters({
      loading: "loading",
      buttonActive: 'buttonActive',
      completeActive: 'completeActive',
    })
  },
  created() {
    this.startWebSocket()
  }
}
</script>

<style scoped>
  .text-complete{
    font-size: 25px;
  }
  .complete-loading{
    text-align: center;
  }
  .icon-complete{
    font-size: 25px;
    margin-left: 20px;
    color: #24de2d;
  }
  .loading-wrapper{
    margin-top: 30px;
  }
  .preloader{
    display: block;
    text-align: center;
  }
  .progress{
    margin-top: 20px;
  }
  .file-upload-input {
    position: absolute;
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    outline: none;
    opacity: 0;
    cursor: pointer;
  }
  .image-upload-wrap {
    margin-top: 20px;
    border: 4px dashed #1FB264;
    position: relative;
    width: 100%;
    height: 60%;
  }
  .text{
    text-align: center;
    width: 500px;
    font-size: 25px;
    position: absolute;
    top: 50%;
    left: 25%;
    transform: translate(0, -50%);
    font-style: italic;
  }
  .btn{
    margin-top: 50px;
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 300px;
    border: 1px solid #807c7e;
    font-weight: bold;
    color: #2a2628;
  }
</style>