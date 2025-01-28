<script setup>
import Typed from 'typed.js';
import { onMounted } from 'vue';

onMounted(() => {
  new Typed('.typed', {
    strings: ["Designer", "Developer", "Freelancer", ],
    typeSpeed: 50,
    backSpeed: 50,
    loop: true
  });
});
</script>

<template>
    <section id="hero" class="hero section dark-background">
      <img src="../assets/images/HeroImage.png" alt="" data-aos="fade-in" />
      <div
        class="container d-flex flex-column align-items-center justify-content-center text-center"
        data-aos="fade-up"
        data-aos-delay="100"
      >
        <h2>I am Ioannis Panaritis</h2>
        <p><span class="typed"></span></p>
      </div>
    </section>
  </template>
  