<template>
  <div class="d-flex flex-column min-vh-10">
    <div class="auth-container flex-grow-1">
      <div class="auth-card">
        <h2 class="text-center mb-3">{{ $t("auth.loginTitle") }}</h2>
        <p class="text-center text-muted">{{ $t("auth.loginSubtitle") }}</p>

        <form @submit.prevent="handleLogin">
          <div class="mb-3">
            <label for="username" class="form-label">{{ $t("auth.username") }}</label>
            <input v-model="username" type="text" class="form-control" id="username" :placeholder="$t('auth.usernamePlaceholder')" required>
          </div>

          <div class="mb-3">
            <label for="password" class="form-label">{{ $t("auth.password") }}</label>
            <input v-model="password" type="password" class="form-control" id="password" :placeholder="$t('auth.passwordPlaceholder')" required>
          </div>

          <button type="submit" class="btn btn-primary w-100">{{ $t("auth.loginButton") }}</button>
        </form>

        <p class="text-center mt-3">
          {{ $t("auth.noAccount") }} <a href="/register" class="text-decoration-none">{{ $t("auth.registerLink") }}</a>
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

</style>
