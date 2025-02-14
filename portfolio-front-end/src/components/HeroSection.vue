<script setup>
import Typed from 'typed.js';
import { onMounted, onUnmounted, ref, watch } from 'vue';
import { useI18n } from 'vue-i18n';

const { t, locale } = useI18n();
const typedInstance = ref(null);

const getStrings = () => {
  return [
    t("hero.role1"),
    t("hero.role2"),
  ];
};

const initTyped = () => {
  if (typedInstance.value) {
    typedInstance.value.destroy();
  }

  typedInstance.value = new Typed('.typed', {
    strings: getStrings(),
    typeSpeed: 50,
    backSpeed: 50,
    loop: true
  });
};

onMounted(() => {
  setTimeout(initTyped, 100);
});

watch(locale, () => {
  setTimeout(initTyped, 100);
});

onUnmounted(() => {
  if (typedInstance.value) {
    typedInstance.value.destroy();
  }
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
      <h2>{{ $t("hero.title") }}</h2>
      <p><span class="typed"></span></p>
    </div>
  </section>
</template>