<template>
  <section id="portfolio" class="portfolio section">
    <div class="container section-title" data-aos="fade-up">
      <h2>Portfolio</h2>
      <p>Here is what I have built</p>
    </div>
    <div class="container">
      <div class="row gy-4" data-aos="fade-up" data-aos-delay="200">
        <div v-for="project in filteredProjects" :key="project.id" class="col-lg-4 col-md-6 portfolio-item">
          <a :href="project.github_link" target="_blank">
            <img :src="project.image" class="img-fluid" alt="Project Image">
          </a>
          <div class="portfolio-info">
            <h4>{{ project.title }}</h4>
            <p>{{ project.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>


<script setup>
import api from '@/services/api';
import { ref, onMounted, computed } from 'vue';

const projects = ref([]); 

//fetch from the api
onMounted(async () => {
  try {
    const response = await api.getAllProjects();
    projects.value = response;
  } catch (error) {
    console.error("Error fetching projects: ", error)
  }
})

const filteredProjects = computed(() => {
  return projects.value.filter(project => project.status === 'shown');
});

</script>

<style scoped>
.portfolio-filters .active {
  font-weight: bold;
  color: #333;
}
</style>
