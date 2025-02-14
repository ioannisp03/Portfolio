<template>
  <div class="container mt-5">
    <div class="card mx-auto" style="max-width: 400px;">
      <div class="card-body">
        <!-- <h2 class="text-center mb-4">Register</h2> -->
        <RegisterForm @register="handleRegister" />
       
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import authService from '@/services/authService';
import RegisterForm from '@/components/RegisterForm.vue';

const router = useRouter();

const handleRegister = async (credentials) => {
  try {
    await authService.register(credentials);
    router.push('/login'); // Redirect to login
  } catch (error) {
    alert("Registration failed", error);
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
