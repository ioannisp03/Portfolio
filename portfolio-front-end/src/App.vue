<script setup>
// import { RouterView } from 'vue-router'
import Footer from './components/FooterComponent.vue';
import HeaderSection from './components/HeaderSection.vue';
</script>

<template>
  <HeaderSection />
  <RouterView />
  <Footer /> 
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}


</style>
