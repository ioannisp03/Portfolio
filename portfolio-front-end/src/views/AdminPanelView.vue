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
                    <a class="nav-link" :class="{ active: currentTab === 'testimonials' }"
                        @click="currentTab = 'testimonials'">
                        Testimonials
                    </a>
                </li>
            </ul>

            <div class="tab-content mt-3">
                <!-- Projects Tab -->
                <div v-if="currentTab === 'projects'">
                    <h2 class="text-center">Projects</h2>
                    <button class="btn btn-primary mb-3" @click="showAddProjectModal">Add Project</button>
                    <div class="table-responsive">
                        <table class="table table-striped table-bordered">
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
                                        <a :href="project.github_link" target="_blank"
                                            class="text-truncate d-inline-block" style="max-width: 150px;">
                                            {{ project.github_link }}
                                        </a>
                                    </td>
                                    <td>{{ project.status }}</td>

                                    <!-- Delete button -->
                                    <td class="d-flex flex-wrap gap-2">
                                        <button @click="deleteProject(project._id)" class="btn btn-danger btn-sm">

                                            <i class="bi bi-x-square-fill"></i>
                                        </button>
                                        <!-- Edit button -->
                                        <button class="btn btn-warning btn-sm">
                                            <i class="bi bi-pencil-square"></i>
                                        </button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Testimonials Tab -->
                <div v-if="currentTab === 'testimonials'">
                    <h2 class="text-center">Testimonials</h2>
                    <button class="btn btn-primary mb-3" @click="showAddTestimonialModal">Add Testimonial</button>
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
                                        <button @click="deleteTestimonial(testimonial._id)"
                                            class="btn btn-danger btn-sm"><i class="bi bi-x-square-fill"></i></button>
                                        <button class="btn btn-warning btn-sm"><i
                                                class="bi bi-pencil-square"></i></button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

        <!-- Modal for adding a proj -->
        <div class="modal fade" id="addProjectModal" tabindex="-1" aria-labelledby="addProjectModalLabel"
            aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="addProjectModalLabel">Add Project</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form @submit.prevent="addProject">
                            <div class="mb-3">
                                <label for="projectName" class="form-label">Name</label>
                                <input type="text" class="form-control" id="projectName" v-model="newProject.name"
                                    required>
                            </div>
                            <div class="mb-3">
                                <label for="projectImage" class="form-label">Image URL</label>
                                <input type="text" class="form-control" id="projectImage" v-model="newProject.image"
                                    required>
                            </div>
                            <div class="mb-3">
                                <label for="projectDescription" class="form-label">Description</label>
                                <textarea class="form-control" id="projectDescription" required
                                    v-model="newProject.description"></textarea>
                            </div>
                            <div class="mb-3">
                                <label for="projectGithubLink" class="form-label">Github Link</label>
                                <input type="text" class="form-control" id="projectGithubLink" required
                                    v-model="newProject.github_link">
                            </div>
                            <div class="mb-3">
                                <label for="projectStatus" class="form-label">Status</label>
                                <select class="form-control" id="projectStatus" v-model="newProject.status" required>
                                    <option value="shown">shown</option>
                                    <option value="hidden">hidden</option>
                                </select>
                            </div>
                            <button type="submit" class="btn btn-primary">Add Project</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>

        <!-- Modal for adding a testimonial -->
        <div class="modal fade" id="addTestimonialModal" tabindex="-1" aria-labelledby="addTestimonialModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="addTestimonialModalLabel">Add Testimonial</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form @submit.prevent="addTestimonial">
                            <div class="mb-3">
                                <label for="testimonialName" class="form-label">Name</label>
                                <input type="text" class="form-control" id="testimonialName" v-model="newTestimonial.name" required>
                            </div>
                            <div class="mb-3">
                                <label for="testimonialTitle" class="form-label">Title</label>
                                <input type="text" class="form-control" id="testimonialTitle" v-model="newTestimonial.title" required>
                            </div>
                            <div class="mb-3">
                                <label for="testimonialMessage" class="form-label">Message</label>
                                <textarea class="form-control" id="testimonialMessage" required v-model="newTestimonial.message"></textarea>
                            </div>
                            <div class="mb-3">
                                <label for="testimonialStatus" class="form-label">Status</label>
                                <select class="form-control" id="testimonialStatus" v-model="newTestimonial.status" required>
                                    <option value="shown">shown</option>
                                    <option value="hidden">hidden</option>
                                </select>
                            </div>
                            <button type="submit" class="btn btn-primary">Add Testimonial</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import api from '@/services/api';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import * as bootstrap from 'bootstrap';

const projects = ref([]);
const testimonials = ref([]);
const currentTab = ref('projects');
const newProject = ref({
    name: '',
    image: '',
    description: '',
    github_link: '',
    status: ''
});
const newTestimonial = ref({
    name: '',
    title: '',
    message: '',
    status: ''
});

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

const showAddProjectModal = () => {
    newProject.value = {}; // reset the new project data
    const addProjectModal = new bootstrap.Modal(document.getElementById('addProjectModal'));
    addProjectModal.show();
};

const showAddTestimonialModal = () => {
    newTestimonial.value = {}; // reset the new testimonial data
    const addTestimonialModal = new bootstrap.Modal(document.getElementById('addTestimonialModal'));
    addTestimonialModal.show();
};

const addProject = async () => {
    try {
        await api.addProjects(newProject.value); // Send new project to backend

        // Fetch updated project list
        const updatedProjects = await api.getAllProjects();
        projects.value = updatedProjects;

        newProject.value = {
            name: '',
            image: '',
            description: '',
            github_link: '',
            status: ''
        };

        // Close modal
        bootstrap.Modal.getInstance(document.getElementById('addProjectModal')).hide();
    } catch (error) {
        console.error("Error adding project: ", error);
    }
};

const addTestimonial = async () => {
    try {
        await api.addTestimonial(newTestimonial.value); 

        // Fetch updated testimonial list
        const updatedTestimonials = await api.getAllTestimonials();
        testimonials.value = updatedTestimonials;

        newTestimonial.value = {
            name: '',
            title: '',
            message: '',
            status: ''
        };

        // Close modal
        bootstrap.Modal.getInstance(document.getElementById('addTestimonialModal')).hide();
    } catch (error) {
        console.error("Error adding testimonial: ", error);
    }
};

const deleteProject = async (projectId) => {

    try {
        // remove project immediately
        projects.value = projects.value.filter(project => project._id !== projectId);

        // delete from the backend
        await api.deleteProject(projectId);

        // fetch latest data from db
        const updatedProjects = await api.getAllProjects();
        projects.value = updatedProjects;


    } catch (error) {
        console.error("Error deleting project: ", error);
    }
};

const deleteTestimonial = async (testimonialId) => {
    try {
        testimonials.value = testimonials.value.filter(testimonial => testimonial._id !== testimonialId);

        await api.deleteTestimonial(testimonialId)

        const updatedTestimonials = await api.getAllTestimonials();
        testimonials.value = updatedTestimonials
    } catch (error) {
        console.error("Error fetching testimonials", error)
    }

}

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