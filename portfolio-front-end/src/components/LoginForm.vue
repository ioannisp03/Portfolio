<template>
  <div class="d-flex flex-column min-vh-10">
    <!-- Main Content -->
    <div class="auth-container flex-grow-1">
      <div class="auth-card">
        <h2 class="text-center mb-3">Welcome Back</h2>
        <p class="text-center text-muted">Log in to continue</p>

        <form @submit.prevent="handleLogin">
          <div class="mb-3">
            <label for="username" class="form-label">Username</label>
            <input v-model="username" type="text" class="form-control" id="username" placeholder="Enter username" required>
          </div>

          <div class="mb-3">
            <label for="password" class="form-label">Password</label>
            <input v-model="password" type="password" class="form-control" id="password" placeholder="Enter password" required>
          </div>

          <button type="submit" class="btn btn-primary w-100">Login</button>
        </form>

        <p class="text-center mt-3">
          Don't have an account? <a href="/register" class="text-decoration-none">Register</a>
        </p>
      </div>
    </div>


  </div>
</template>

<script setup>
import { ref, defineEmits } from 'vue';

const username = ref('');
const password = ref('');
const emit = defineEmits(['login']);

const handleLogin = () => {
  emit('login', { username: username.value, password: password.value });
};
</script>

<style scoped>
/* 🌟 Layout Fix */
.d-flex {
  display: flex;
  flex-direction: column;
}

.flex-grow-1 {
  flex-grow: 1;
}

.min-vh-100 {
  min-height: 100vh;
}

/* 🌟 Auth Styles */
.auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 15px;
}

.auth-card {
  background: white;
  padding: 25px;
  border-radius: 10px;
  box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 380px;
  text-align: center;
}

/* 🌟 Footer */
.footer {
  background: #343a40;
  color: white;
}
</style>
