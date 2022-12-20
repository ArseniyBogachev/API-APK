import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: () => ({
    api_keys: [],
    ws: null,
    filename: '',
    loading: 1,
    buttonActive: true,
    completeActive: true,
  }),
  getters: {
    api_keys(state){
      return state.api_keys
    },
    ws(state){
      return state.ws
    },
    filename(state){
      return state.filename
    },
    loading(state){
      return state.loading
    },
    buttonActive(state){
      return state.buttonActive
    },
    completeActive(state){
      return state.completeActive
    },
  },
  mutations: {
    ApiKeys(state, api_keys){
      state.api_keys = api_keys
    },
    webSocket(state, ws){
      state.ws = ws
    },
    FileName(state, filename){
      state.filename = filename
    },
    Loading(state, loading){
      state.loading = loading
    },
    ButtonActive(state){
      state.buttonActive = !state.buttonActive
    },
    CompleteActive(state){
      state.completeActive = !state.completeActive
    },
  },
  actions: {
    async post_file(ctx, upload_file){
      try{
        ctx.commit('ButtonActive')
        let formData = new FormData();
        formData.append('file', upload_file)
        const response = await axios.post('http://127.0.0.1:8000/upload/', formData)
        await ctx.commit('FileName', response.data)
        await ctx.getters.ws.send(ctx.getters.filename)
      }
      catch (e) {
        console.log(e)
      }
    },
    async startWebSocket(ctx) {
      console.log("Starting connection to WebSocket Server")
      const ws = await new WebSocket("ws://localhost:8000/ws")
      ctx.commit('webSocket', ws)
      ws.onmessage = await function(event) {
        if (Number(event.data)){
          ctx.commit('Loading', Number(event.data))
        }
        else{
          ctx.commit('ApiKeys', JSON.parse(event.data))
          ctx.commit('Loading', 0)
          ctx.commit('CompleteActive')
        }
      };
      ws.onerror = await function(event) {
        console.log(event);
      };
  }
  },
  modules: {
  }
})
