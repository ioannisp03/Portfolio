<script setup>
import { ref, onMounted } from 'vue';
import api from '@/services/api';

const projects = ref([]);
const testimonials = ref([]);
const currentTab = ref('projects'); // manage the active tab

onMounted(async () => {
    try {
        const projectsResponse = await api.getAllProjects();
        projects.value = projectsResponse;
    } catch (error) {
        console.error("Error fetching projects: ", error);
    }

    try {
        const testimonialsResponse = await api.getAllTestimonials();
        testimonials.value = testimonialsResponse;
    } catch (error) {
        console.error("Error fetching testimonials: ", error);
    }
});
</script>

<template>
    <div class="d-flex flex-column min-vh-100">
        <div class="container mt-4 flex-grow-1">
            <!-- Responsive Tab Navigation -->
            <ul class="nav nav-tabs justify-content-left">
                <li class="nav-item">
                    <a class="nav-link" :class="{ active: currentTab === 'projects' }" @click="currentTab = 'projects'">
                        Projects
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" :class="{ active: currentTab === 'testimonials' }" @click="currentTab = 'testimonials'">
                        Testimonials
                    </a>
                </li>
            </ul>

            <div class="tab-content mt-3">
                <!-- Projects Tab -->
                <div v-if="currentTab === 'projects'">
                    <h2 class="text-center">Projects</h2>
                    <div class="table-responsive">
                        <table class="table table-striped table-bordered ">
                            <thead class="thead-light">
                                <tr>
                                    <th>Name</th>
                                    <th>Image</th>
                                    <th>Description</th>
                                    <th>Github Link</th>
                                    <th>Status</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="project in projects" :key="project.id">
                                    <td>{{ project.name }}</td>
                                    <td>
                                        <img :src="project.image" class="img-fluid img-thumbnail" alt="Project Image">
                                    </td>
                                    <td class="text-truncate" style="max-width: 200px;">{{ project.description }}</td>
                                    <td>
                                        <a :href="project.github_link" target="_blank" class="text-truncate d-inline-block" style="max-width: 150px;">
                                            {{ project.github_link }}
                                        </a>
                                    </td>
                                    <td>{{ project.status }}</td>
                                    <td class="d-flex flex-wrap gap-2">
                                        <button class="btn btn-danger btn-sm"><i class="bi bi-x-square-fill"></i></button>
                                        <button class="btn btn-warning btn-sm"><i class="bi bi-pencil-square"></i></button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Testimonials Tab -->
                <div v-if="currentTab === 'testimonials'">
                    <h2 class="text-center">Testimonials</h2>
                    <div class="table-responsive">
                        <table class="table table-striped table-bordered">
                            <thead class="thead-light">
                                <tr>
                                    <th>Name</th>
                                    <th>Title</th>
                                    <th>Message</th>
                                    <th>Status</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="testimonial in testimonials" :key="testimonial.id">
                                    <td>{{ testimonial.name }}</td>
                                    <td>{{ testimonial.title }}</td>
                                    <td class="text-truncate" style="max-width: 200px;">{{ testimonial.message }}</td>
                                    <td>{{ testimonial.status }}</td>
                                    <td class="d-flex flex-wrap gap-2">
                                        <button class="btn btn-danger btn-sm"><i class="bi bi-x-square-fill"></i></button>
                                        <button class="btn btn-primary btn-sm"><i class="bi bi-pencil-square"></i></button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

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

/* Make tables scrollable on small screens */
.table-responsive {
    overflow-x: auto;
}

/* Improve button spacing */
.gap-2 {
    gap: 8px;
}

/* Make images responsive */
.img-thumbnail {
    max-width: 100px;
    height: auto;
}
</style>
