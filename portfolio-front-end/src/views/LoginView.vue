<template>
  <div class="container mt-5">
    <div class="card mx-auto" style="max-width: 400px;">
      <div class="card-body">
        <h2 class="text-center mb-4">Login</h2>
        <LoginForm @login="handleLogin" />
       
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import authService from '@/services/authService';
import LoginForm from '@/components/LoginForm.vue';

const router = useRouter();

const handleLogin = async (credentials) => {
  try {
    await authService.login(credentials);
    router.push('/'); // Redirect home after login
  } catch (error) {
    alert("Login failed", error);
  }
};
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.card {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.card-body {
  padding: 2rem;
}

h2 {
  font-size: 1.5rem;
  font-weight: bold;
}

p {
  font-size: 0.875rem;
}

a {
  color: #007bff;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
</style>
