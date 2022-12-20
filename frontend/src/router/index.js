import { createRouter, createWebHistory } from 'vue-router'
import UploadApp from "@/pages/UploadApp";
import ApiApp from "@/pages/ApiApp";

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
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
