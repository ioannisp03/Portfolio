<template>
    <div class="d-flex flex-column min-vh-100">
        <div class="container mt-4 flex-grow-1">
            <!-- Responsive Tab Navigation -->
            <ul class="nav nav-tabs justify-content-left">
                <li class="nav-item">
                    <a class="nav-link" :class="{ active: currentTab === 'projects' }" @click="currentTab = 'projects'">
                        {{ $t('adminPanel.projects') }}
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" :class="{ active: currentTab === 'testimonials' }" @click="currentTab = 'testimonials'">
                        {{ $t('adminPanel.testimonials') }}
                    </a>
                </li>
            </ul>

            <div class="tab-content mt-3">
                <!-- Projects Tab -->
                <div v-if="currentTab === 'projects'">
                    <h2 class="text-center">{{ $t('adminPanel.projects') }}</h2>
                    <button class="btn btn-primary mb-3" @click="showAddProjectModal">
                        {{ $t('adminPanel.buttons.addProject') }}
                    </button>
                    <div class="table-responsive">
                        <table class="table table-striped table-bordered">
                            <thead class="thead-light">
                                <tr>
                                    <th>{{ $t('adminPanel.projectFields.name') }}</th>
                                    <th>{{ $t('adminPanel.projectFields.image') }}</th>
                                    <th>{{ $t('adminPanel.projectFields.description') }}</th>
                                    <th>{{ $t('adminPanel.projectFields.githubLink') }}</th>
                                    <th>{{ $t('adminPanel.projectFields.status') }}</th>
                                    <th>{{ $t('adminPanel.projectFields.actions') }}</th>
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
                                    <td :class="{ 'text-success': project.status === 'shown', 'text-danger': project.status === 'hidden' }">
                                        {{ $t(`adminPanel.statusOptions.${project.status}`) }}
                                    </td>
                                    <td class="d-flex flex-wrap gap-2">
                                        <button @click="deleteProject(project._id)" class="btn btn-danger btn-sm">
                                            <i class="bi bi-x-square-fill"></i>
                                            {{ $t('adminPanel.buttons.delete') }}
                                        </button>
                                        <button @click="showUpdateProjectModal(project)" class="btn btn-warning btn-sm">
                                            <i class="bi bi-pencil-square"></i>
                                            {{ $t('adminPanel.buttons.edit') }}
                                        </button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Testimonials Tab -->
                <div v-if="currentTab === 'testimonials'">
                    <h2 class="text-center">{{ $t('adminPanel.testimonials') }}</h2>
                    <button class="btn btn-primary mb-3" @click="showAddTestimonialModal">
                        {{ $t('adminPanel.buttons.addTestimonial') }}
                    </button>
                    <div class="table-responsive">
                        <table class="table table-striped table-bordered">
                            <thead class="thead-light">
                                <tr>
                                    <th>{{ $t('adminPanel.testimonialFields.name') }}</th>
                                    <th>{{ $t('adminPanel.testimonialFields.title') }}</th>
                                    <th>{{ $t('adminPanel.testimonialFields.message') }}</th>
                                    <th>{{ $t('adminPanel.testimonialFields.status') }}</th>
                                    <th>{{ $t('adminPanel.testimonialFields.actions') }}</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="testimonial in testimonials" :key="testimonial.id">
                                    <td>{{ testimonial.name }}</td>
                                    <td>{{ testimonial.title }}</td>
                                    <td class="text-truncate" style="max-width: 200px;">{{ testimonial.message }}</td>
                                    <td :class="{ 'text-success': testimonial.status === 'shown', 'text-danger': testimonial.status === 'hidden' }">
                                        {{ $t(`adminPanel.statusOptions.${testimonial.status}`) }}
                                    </td>
                                    <td class="d-flex flex-wrap gap-2">
                                        <button @click="deleteTestimonial(testimonial._id)" class="btn btn-danger btn-sm">
                                            <i class="bi bi-x-square-fill"></i>
                                            {{ $t('adminPanel.buttons.delete') }}
                                        </button>
                                        <button @click="showUpdateTestimonialModal(testimonial)" class="btn btn-warning btn-sm">
                                            <i class="bi bi-pencil-square"></i>
                                            {{ $t('adminPanel.buttons.edit') }}
                                        </button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

        <!-- Modal for adding a project -->
        <div class="modal fade" id="addProjectModal" tabindex="-1" aria-labelledby="addProjectModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="addProjectModalLabel">{{ $t('adminPanel.modalTitleAddProject') }}</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form @submit.prevent="addProject">
                            <div class="mb-3">
                                <label for="projectName" class="form-label">{{ $t('adminPanel.projectFields.name') }}</label>
                                <input type="text" class="form-control" id="projectName" v-model="newProject.name" required>
                            </div>
                            <div class="mb-3">
                                <label for="projectImage" class="form-label">{{ $t('adminPanel.projectFields.image') }}</label>
                                <input type="text" class="form-control" id="projectImage" v-model="newProject.image" required>
                            </div>
                            <div class="mb-3">
                                <label for="projectDescription" class="form-label">{{ $t('adminPanel.projectFields.description') }}</label>
                                <textarea class="form-control" id="projectDescription" required v-model="newProject.description"></textarea>
                            </div>
                            <div class="mb-3">
                                <label for="projectGithubLink" class="form-label">{{ $t('adminPanel.projectFields.githubLink') }}</label>
                                <input type="text" class="form-control" id="projectGithubLink" required v-model="newProject.github_link">
                            </div>
                            <div class="mb-3">
                                <label for="projectStatus" class="form-label">{{ $t('adminPanel.projectFields.status') }}</label>
                                <select class="form-control" id="projectStatus" v-model="newProject.status" required>
                                    <option value="shown">{{ $t('adminPanel.statusOptions.shown') }}</option>
                                    <option value="hidden">{{ $t('adminPanel.statusOptions.hidden') }}</option>
                                </select>
                            </div>
                            <button type="submit" class="btn btn-primary">
                                {{ $t('adminPanel.buttons.addProject') }}
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>

        <!-- Modal for updating a project -->
        <div class="modal fade" id="updateProjectModal" tabindex="-1" aria-labelledby="updateProjectModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="updateProjectModalLabel">{{ $t('adminPanel.modalTitleUpdateProject') }}</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form @submit.prevent="updateProject">
                            <div class="mb-3">
                                <label for="updateProjectName" class="form-label">{{ $t('adminPanel.projectFields.name') }}</label>
                                <input type="text" class="form-control" id="updateProjectName" v-model="currentProject.name" required>
                            </div>
                            <div class="mb-3">
                                <label for="updateProjectImage" class="form-label">{{ $t('adminPanel.projectFields.image') }}</label>
                                <input type="text" class="form-control" id="updateProjectImage" v-model="currentProject.image" required>
                            </div>
                            <div class="mb-3">
                                <label for="updateProjectDescription" class="form-label">{{ $t('adminPanel.projectFields.description') }}</label>
                                <textarea class="form-control" id="updateProjectDescription" required v-model="currentProject.description"></textarea>
                            </div>
                            <div class="mb-3">
                                <label for="updateProjectGithubLink" class="form-label">{{ $t('adminPanel.projectFields.githubLink') }}</label>
                                <input type="text" class="form-control" id="updateProjectGithubLink" required v-model="currentProject.github_link">
                            </div>
                            <div class="mb-3">
                                <label for="updateProjectStatus" class="form-label">{{ $t('adminPanel.projectFields.status') }}</label>
                                <select class="form-control" id="updateProjectStatus" v-model="currentProject.status" required>
                                    <option value="shown">{{ $t('adminPanel.statusOptions.shown') }}</option>
                                    <option value="hidden">{{ $t('adminPanel.statusOptions.hidden') }}</option>
                                </select>
                            </div>
                            <button type="submit" class="btn btn-primary">
                                {{ $t('adminPanel.buttons.updateProject') }}
                            </button>
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
                        <h5 class="modal-title" id="addTestimonialModalLabel">{{ $t('adminPanel.modalTitleAddTestimonial') }}</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form @submit.prevent="addTestimonial">
                            <div class="mb-3">
                                <label for="testimonialName" class="form-label">{{ $t('adminPanel.testimonialFields.name') }}</label>
                                <input type="text" class="form-control" id="testimonialName" v-model="newTestimonial.name" required>
                            </div>
                            <div class="mb-3">
                                <label for="testimonialTitle" class="form-label">{{ $t('adminPanel.testimonialFields.title') }}</label>
                                <input type="text" class="form-control" id="testimonialTitle" v-model="newTestimonial.title" required>
                            </div>
                            <div class="mb-3">
                                <label for="testimonialMessage" class="form-label">{{ $t('adminPanel.testimonialFields.message') }}</label>
                                <textarea class="form-control" id="testimonialMessage" required v-model="newTestimonial.message"></textarea>
                            </div>
                            <div class="mb-3">
                                <label for="testimonialStatus" class="form-label">{{ $t('adminPanel.testimonialFields.status') }}</label>
                                <select class="form-control" id="testimonialStatus" v-model="newTestimonial.status" required>
                                    <option value="shown">{{ $t('adminPanel.statusOptions.shown') }}</option>
                                    <option value="hidden">{{ $t('adminPanel.statusOptions.hidden') }}</option>
                                </select>
                            </div>
                            <button type="submit" class="btn btn-primary">
                                {{ $t('adminPanel.buttons.addTestimonial') }}
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>

        <!-- Modal for updating a testimonial -->
        <div class="modal fade" id="updateTestimonialModal" tabindex="-1" aria-labelledby="updateTestimonialModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="updateTestimonialModalLabel">{{ $t('adminPanel.modalTitleUpdateTestimonial') }}</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form @submit.prevent="updateTestimonial">
                            <div class="mb-3">
                                <label for="updateTestimonialName" class="form-label">{{ $t('adminPanel.testimonialFields.name') }}</label>
                                <input type="text" class="form-control" id="updateTestimonialName" v-model="currentTestimonial.name" required>
                            </div>
                            <div class="mb-3">
                                <label for="updateTestimonialTitle" class="form-label">{{ $t('adminPanel.testimonialFields.title') }}</label>
                                <input type="text" class="form-control" id="updateTestimonialTitle" v-model="currentTestimonial.title" required>
                            </div>
                            <div class="mb-3">
                                <label for="updateTestimonialMessage" class="form-label">{{ $t('adminPanel.testimonialFields.message') }}</label>
                                <textarea class="form-control" id="updateTestimonialMessage" required v-model="currentTestimonial.message"></textarea>
                            </div>
                            <div class="mb-3">
                                <label for="updateTestimonialStatus" class="form-label">{{ $t('adminPanel.testimonialFields.status') }}</label>
                                <select class="form-control" id="updateTestimonialStatus" v-model="currentTestimonial.status" required>
                                    <option value="shown">{{ $t('adminPanel.statusOptions.shown') }}</option>
                                    <option value="hidden">{{ $t('adminPanel.statusOptions.hidden') }}</option>
                                </select>
                            </div>
                            <button type="submit" class="btn btn-primary">
                                {{ $t('adminPanel.buttons.updateTestimonial') }}
                            </button>
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
const currentProject = ref({});
const currentTestimonial = ref({});

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

const showUpdateProjectModal = (project) => {
    currentProject.value = { ...project }; // preload the project data
    const updateProjectModal = new bootstrap.Modal(document.getElementById('updateProjectModal'));
    updateProjectModal.show();
};

const showAddTestimonialModal = () => {
    newTestimonial.value = {}; // reset the new testimonial data
    const addTestimonialModal = new bootstrap.Modal(document.getElementById('addTestimonialModal'));
    addTestimonialModal.show();
};

const showUpdateTestimonialModal = (testimonial) => {
    currentTestimonial.value = { ...testimonial }; // preload the testimonial data
    const updateTestimonialModal = new bootstrap.Modal(document.getElementById('updateTestimonialModal'));
    updateTestimonialModal.show();
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

const updateProject = async () => {
    console.log(currentProject.value)
    try {
        await api.updateProject(currentProject.value); // Send updated project to backend

        // Fetch updated project list
        const updatedProjects = await api.getAllProjects();
        projects.value = updatedProjects;

        // Close modal
        bootstrap.Modal.getInstance(document.getElementById('updateProjectModal')).hide();
    } catch (error) {
        console.error("Error updating project: ", error);
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

const updateTestimonial = async () => {
    console.log("Current Testimonial:", currentTestimonial.value); // Log the current testimonial

  if (!currentTestimonial.value._id || currentTestimonial.value._id === 'undefined') {
    console.error("Invalid testimonial ID:", currentTestimonial.value._id);
    return;
  }
    try {
        await api.updateTestimonial(currentTestimonial.value); // Send updated testimonial to backend

        // Fetch updated testimonial list
        const updatedTestimonials = await api.getAllTestimonials();
        testimonials.value = updatedTestimonials;

        // Close modal
        bootstrap.Modal.getInstance(document.getElementById('updateTestimonialModal')).hide();
    } catch (error) {
        console.error("Error updating testimonial: ", error);
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