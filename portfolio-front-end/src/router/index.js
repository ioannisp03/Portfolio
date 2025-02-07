import AdminPanelView from '@/views/AdminPanelView.vue'
import HomeView from '@/views/HomeView.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/admin-panel',
      name: 'admin-panel',
      component: AdminPanelView
    }
  ],
})

export default router
