<template>
  <section id="portfolio" class="portfolio section">
    <div class="container section-title" data-aos="fade-up">
      <h2>{{ $t("portfolio.title") }}</h2>
      <p>{{ $t("portfolio.subtitle") }}</p>
    </div>

    <div class="container">
      <div class="row gy-4" data-aos="fade-up" data-aos-delay="200">
        <!-- Use project._id as key and display localized name/description -->
        <div v-for="project in filteredProjects" :key="project._id" class="col-lg-4 col-md-6 portfolio-item">
          <a :href="project.github_link" target="_blank">
            <img
              :src="project.image"
              class="img-fluid"
              alt="Project Image"
              style="width: 100%; height: 200px; object-fit: cover; border-radius: 2px; border: 1px solid black;"
            />
          </a>
          <div class="portfolio-info">
            <h4>{{ project.name[$i18n.locale] || project.name.en }}</h4>
            <p>{{ project.description[$i18n.locale] || project.description.en }}</p>
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

// Fetch from the API on mount
onMounted(async () => {
  try {
    const response = await api.getAllProjects();
    projects.value = response;
  } catch (error) {
    console.error("Error fetching projects: ", error);
  }
});

// Only show projects with status "shown"
const filteredProjects = computed(() => {
  return projects.value.filter(project => project.status === 'shown');
});
</script>

<style scoped>
.portfolio-filters .active {
  font-weight: bold;
  color: #333;
}

.portfolio-item {
  transition: transform 0.3s ease;
}

.portfolio-item:hover {
  transform: scale(1.05);
}

.portfolio-info {
  background-color: #fff;
  padding: 15px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-top: -20px;
  position: relative;
  z-index: 1;
}

.portfolio-info h4 {
  font-size: 1.25rem;
  margin-bottom: 10px;
}

.portfolio-info p {
  font-size: 0.875rem;
  color: #666;
}
</style>
