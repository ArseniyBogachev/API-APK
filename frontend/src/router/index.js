import { createRouter, createWebHistory } from 'vue-router'
import UploadApp from "@/pages/UploadApp";
import ApiApp from "@/pages/ApiApp";
import ListApp from "@/pages/ListApp";

const routes = [
  {
    path: '/',
    name: 'upload',
    component: UploadApp
  },
  {
    path: '/api',
    name: 'api',
    component: ApiApp
  },
  {
    path: '/list',
    name: 'list',
    component: ListApp
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
