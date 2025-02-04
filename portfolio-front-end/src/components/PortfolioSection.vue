<template>
  <!-- Portfolio Section -->
  <section id="portfolio" class="portfolio section">

    <!-- Section Title -->
    <div class="container section-title" data-aos="fade-up">
      <h2>Portfolio</h2>
      <p>Here is what I have built</p>
    </div>

    <div class="container">
      <div class="row gy-4" data-aos="fade-up" data-aos-delay="200">
        <!-- Loop through all projects -->
        <div v-for="project in projects" :key="project.id" class="col-lg-4 col-md-6 portfolio-item">
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
import { ref, onMounted } from 'vue';

const projects = ref([]); //holds the array of objects

//fetch from the api
onMounted(async () => {
  try{
    const response = await api.getAllProjects();
    projects.value = response;
  }catch(error){
    console.error("Error fetching projects: ",error)
  }
})

</script>

<style scoped>
.portfolio-filters .active {
  font-weight: bold;
  color: #333;
}
</style>
