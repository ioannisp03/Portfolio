import AdminPanelView from '@/views/AdminPanelView.vue'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import RegisterView from '@/views/RegisterView.vue'
import { createRouter, createWebHistory } from 'vue-router'
import authService from '@/services/authService'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },
    {
      path: '/admin-panel',
      name: 'admin-panel',
      component: AdminPanelView,
      meta: { requiresAuth: true, requiresAdmin: true } //protects admin panel route
    }

  ],
})

router.beforeEach(async(to, from, next) => {
  if(to.meta.requiresAuth || to.meta.requiresAdmin){
    const user  = await authService.getUser();
    if (!user) {
      return next('/login'); // Redirect to login if not logged in
    }
    if (to.meta.requiresAdmin && user.role !== 'admin') {
      return next('/'); // Redirect if not an admin
    }
  }
  next();
});

export default router;
