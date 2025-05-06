vue
<template>
  <div class="modal fade" id="confirmDeleteModal" tabindex="-1" aria-labelledby="confirmDeleteModalLabel"
    aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="confirmDeleteModalLabel">{{ $t('adminPanel.confirmDeleteTitle') }}</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          {{ confirmDeleteMessage }}
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">{{ $t('adminPanel.buttons.cancel')
            }}</button>
          <button type="button" class="btn btn-danger" @click="confirmDelete">{{ $t('adminPanel.buttons.confirm')
            }}</button>
        </div>
      </div>
    </div>
  </div>

  <div class="d-flex flex-column min-vh-100">
    <div class="container mt-4 flex-grow-1">
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
                <tr v-for="project in projects" :key="project._id">
                  <td>{{ project.name[$i18n.locale] || project.name.en }}</td>
                  <td>
                    <img :src="project.image" class="img-fluid img-thumbnail" alt="Project Image">
                  </td>
                  <td class="text-truncate" style="max-width: 200px;">
                    {{ project.description[$i18n.locale] || project.description.en }}
                  </td>
                  <td>
                    <a :href="project.github_link" target="_blank" class="text-truncate d-inline-block"
                      style="max-width: 150px;">
                      {{ project.github_link }}
                    </a>
                  </td>
                  <td
                    :class="{ 'text-success': project.status === 'shown', 'text-danger': project.status === 'hidden' }">
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
                <tr v-for="testimonial in testimonials" :key="testimonial._id">
                  <td>{{ testimonial.name }}</td>
                  <td>{{ testimonial.title }}</td>
                  <td class="text-truncate" style="max-width: 200px;">{{ testimonial.message }}</td>
                  <td
                    :class="{ 'text-success': testimonial.status === 'shown', 'text-danger': testimonial.status === 'hidden' }">
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

    <!-- Modal for Adding a Project -->
    <div class="modal fade" id="addProjectModal" tabindex="-1" aria-labelledby="addProjectModalLabel"
      aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="addProjectModalLabel">{{ $t('adminPanel.modalTitleAddProject') }}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="addProject">
              <div class="mb-3">
                <label for="projectNameEn" class="form-label">Name (English)</label>
                <input type="text" class="form-control" id="projectNameEn" v-model="newProject.name.en" required>
              </div>
              <div class="mb-3">
                <label for="projectNameFr" class="form-label">Name (French)</label>
                <input type="text" class="form-control" id="projectNameFr" v-model="newProject.name.fr" required>
              </div>
              <div class="mb-3">
                <label for="projectImage" class="form-label">{{ $t('adminPanel.projectFields.image') }}</label>
                <input type="text" class="form-control" id="projectImage" v-model="newProject.image" required>
              </div>
              <div class="mb-3">
                <label for="projectDescriptionEn" class="form-label">Description (English)</label>
                <textarea class="form-control" id="projectDescriptionEn" required
                  v-model="newProject.description.en"></textarea>
              </div>
              <div class="mb-3">
                <label for="projectDescriptionFr" class="form-label">Description (French)</label>
                <textarea class="form-control" id="projectDescriptionFr" required
                  v-model="newProject.description.fr"></textarea>
              </div>
              <div class="mb-3">
                <label for="projectGithubLink" class="form-label">{{ $t('adminPanel.projectFields.githubLink')
                }}</label>
                <input type="text" class="form-control" id="projectGithubLink" required
                  v-model="newProject.github_link">
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

    <!-- Modal for Updating a Project -->
    <div class="modal fade" id="updateProjectModal" tabindex="-1" aria-labelledby="updateProjectModalLabel"
      aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="updateProjectModalLabel">{{ $t('adminPanel.modalTitleUpdateProject') }}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="updateProject">
              <div class="mb-3">
                <label for="editProjectNameEn" class="form-label">Name (English)</label>
                <input type="text" class="form-control" id="editProjectNameEn" v-model="currentProject.name.en"
                  required>
              </div>
              <div class="mb-3">
                <label for="editProjectNameFr" class="form-label">Name (French)</label>
                <input type="text" class="form-control" id="editProjectNameFr" v-model="currentProject.name.fr"
                  required>
              </div>
              <div class="mb-3">
                <label for="editProjectImage" class="form-label">{{ $t('adminPanel.projectFields.image') }}</label>
                <input type="text" class="form-control" id="editProjectImage" v-model="currentProject.image" required>
              </div>
              <div class="mb-3">
                <label for="editProjectDescriptionEn" class="form-label">Description (English)</label>
                <textarea class="form-control" id="editProjectDescriptionEn" required
                  v-model="currentProject.description.en"></textarea>
              </div>
              <div class="mb-3">
                <label for="editProjectDescriptionFr" class="form-label">Description (French)</label>
                <textarea class="form-control" id="editProjectDescriptionFr" required
                  v-model="currentProject.description.fr"></textarea>
              </div>
              <div class="mb-3">
                <label for="editProjectGithubLink" class="form-label">{{ $t('adminPanel.projectFields.githubLink')
                }}</label>
                <input type="text" class="form-control" id="editProjectGithubLink" required
                  v-model="currentProject.github_link">
              </div>
              <div class="mb-3">
                <label for="editProjectStatus" class="form-label">{{ $t('adminPanel.projectFields.status') }}</label>
                <select class="form-control" id="editProjectStatus" v-model="currentProject.status" required>
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

    <!-- Modal for Adding a Testimonial -->
    <div class="modal fade" id="addTestimonialModal" tabindex="-1" aria-labelledby="addTestimonialModalLabel"
      aria-hidden="true">
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
                <label for="testimonialMessage" class="form-label">{{ $t('adminPanel.testimonialFields.message')
                }}</label>
                <textarea class="form-control" id="testimonialMessage" required
                  v-model="newTestimonial.message"></textarea>
              </div>
              <div class="mb-3">
                <label for="testimonialStatus" class="form-label">{{ $t('adminPanel.testimonialFields.status')
                }}</label>
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

    <!-- Modal for Updating a Testimonial -->
    <div class="modal fade" id="updateTestimonialModal" tabindex="-1" aria-labelledby="updateTestimonialModalLabel"
      aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="updateTestimonialModalLabel">{{ $t('adminPanel.modalTitleUpdateTestimonial') }}
            </h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="updateTestimonial">
              <div class="mb-3">
                <label for="editTestimonialName" class="form-label">{{ $t('adminPanel.testimonialFields.name')
                }}</label>
                <input type="text" class="form-control" id="editTestimonialName" v-model="currentTestimonial.name"
                  required>
              </div>
              <div class="mb-3">
                <label for="editTestimonialTitle" class="form-label">{{ $t('adminPanel.testimonialFields.title')
                }}</label>
                <input type="text" class="form-control" id="editTestimonialTitle" v-model="currentTestimonial.title"
                  required>
              </div>
              <div class="mb-3">
                <label for="editTestimonialMessage" class="form-label">{{ $t('adminPanel.testimonialFields.message')
                }}</label>
                <textarea class="form-control" id="editTestimonialMessage" required
                  v-model="currentTestimonial.message"></textarea>
              </div>
              <div class="mb-3">
                <label for="editTestimonialStatus" class="form-label">{{ $t('adminPanel.testimonialFields.status')
                }}</label>
                <select class="form-control" id="editTestimonialStatus" v-model="currentTestimonial.status" required>
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
import { useI18n } from 'vue-i18n';
import Toastify from 'toastify-js';
import "toastify-js/src/toastify.css";

const { t } = useI18n();

const projects = ref([]);
const testimonials = ref([]);
const currentTab = ref('projects');

// Add these for custom confirmation modal
const confirmDeleteMessage = ref('');
const deleteItemId = ref(null);
const deleteItemType = ref(''); // 'project' or 'testimonial'
const confirmDeleteModal = ref(null);

const newProject = ref({
  name: {
    en: '',
    fr: ''
  },
  image: '',
  description: {
    en: '',
    fr: ''
  },
  github_link: '',
  status: 'shown'
});

const newTestimonial = ref({
  name: '',
  title: '',
  message: '',
  status: 'shown'
});

const currentProject = ref({
  _id: '',
  name: {
    en: '',
    fr: ''
  },
  image: '',
  description: {
    en: '',
    fr: ''
  },
  github_link: '',
  status: 'shown'
});

const currentTestimonial = ref({});

onMounted(async () => {
  try {
    const projectsResponse = await api.getAllProjects();
    projects.value = projectsResponse;
  } catch (error) {
    console.error("Error fetching projects:", error);
  }

  try {
    const testimonialsResponse = await api.getAllTestimonials();
    testimonials.value = testimonialsResponse;
  } catch (error) {
    console.error("Error fetching testimonials:", error);
  }
  
  // Initialize the confirmDeleteModal ref after the component is mounted
  confirmDeleteModal.value = new bootstrap.Modal(document.getElementById('confirmDeleteModal'));
});

const showAddProjectModal = () => {
  newProject.value = {
    name: { en: '', fr: '' },
    image: '',
    description: { en: '', fr: '' },
    github_link: '',
    status: 'shown'
  };
  const addProjectModal = new bootstrap.Modal(document.getElementById('addProjectModal'));
  addProjectModal.show();
};

const showUpdateProjectModal = (project) => {
  currentProject.value = { ...project };
  const updateProjectModal = new bootstrap.Modal(document.getElementById('updateProjectModal'));
  updateProjectModal.show();
};

const showAddTestimonialModal = () => {
  newTestimonial.value = {
    name: '',
    title: '',
    message: '',
    status: 'shown'
  };
  const addTestimonialModal = new bootstrap.Modal(document.getElementById('addTestimonialModal'));
  addTestimonialModal.show();
};

const showUpdateTestimonialModal = (testimonial) => {
  currentTestimonial.value = { ...testimonial };
  const updateTestimonialModal = new bootstrap.Modal(document.getElementById('updateTestimonialModal'));
  updateTestimonialModal.show();
};

const addProject = async () => {
  try {
    await api.addProjects(newProject.value);
    const updatedProjects = await api.getAllProjects();
    projects.value = updatedProjects;
    newProject.value = {
      name: { en: '', fr: '' },
      image: '',
      description: { en: '', fr: '' },
      github_link: '',
      status: 'shown'
    };
    bootstrap.Modal.getInstance(document.getElementById('addProjectModal')).hide();
    
    // Show success toast
    Toastify({
      text: t('adminPanel.notifications.projectAdded'),
      duration: 3000,
      close: true,
      gravity: "top",
      position: "right",
      backgroundColor: "#4caf50",
      stopOnFocus: true
    }).showToast();
  } catch (error) {
    console.error("Error adding project:", error);
    
    // Show error toast
    Toastify({
      text: t('adminPanel.notifications.projectAddError'),
      duration: 3000,
      close: true,
      gravity: "top",
      position: "right",
      backgroundColor: "#f44336",
      stopOnFocus: true
    }).showToast();
  }
};

const updateProject = async () => {
  try {
    await api.updateProject(currentProject.value);
    const updatedProjects = await api.getAllProjects();
    projects.value = updatedProjects;
    bootstrap.Modal.getInstance(document.getElementById('updateProjectModal')).hide();
    
    // Show success toast
    Toastify({
      text: t('adminPanel.notifications.projectUpdated'),
      duration: 3000,
      close: true,
      gravity: "top",
      position: "right",
      backgroundColor: "#4caf50",
      stopOnFocus: true
    }).showToast();
  } catch (error) {
    console.error("Error updating project:", error);
    
    // Show error toast
    Toastify({
      text: t('adminPanel.notifications.projectUpdateError'),
      duration: 3000,
      close: true,
      gravity: "top",
      position: "right",
      backgroundColor: "#f44336",
      stopOnFocus: true
    }).showToast();
  }
};

const addTestimonial = async () => {
  try {
    await api.addTestimonial(newTestimonial.value);
    const updatedTestimonials = await api.getAllTestimonials();
    testimonials.value = updatedTestimonials;
    newTestimonial.value = {
      name: '',
      title: '',
      message: '',
      status: 'shown'
    };
    bootstrap.Modal.getInstance(document.getElementById('addTestimonialModal')).hide();
    
    // Show success toast
    Toastify({
      text: t('adminPanel.notifications.testimonialAdded'),
      duration: 3000,
      close: true,
      gravity: "top",
      position: "right",
      backgroundColor: "#4caf50",
      stopOnFocus: true
    }).showToast();
  } catch (error) {
    console.error("Error adding testimonial:", error);
    
    // Show error toast
    Toastify({
      text: t('adminPanel.notifications.testimonialAddError'),
      duration: 3000,
      close: true,
      gravity: "top",
      position: "right",
      backgroundColor: "#f44336",
      stopOnFocus: true
    }).showToast();
  }
};

const updateTestimonial = async () => {
  if (!currentTestimonial.value._id) {
    console.error("Invalid testimonial ID:", currentTestimonial.value._id);
    
    // Show error toast
    Toastify({
      text: t('adminPanel.notifications.invalidTestimonialId'),
      duration: 3000,
      close: true,
      gravity: "top",
      position: "right",
      backgroundColor: "#f44336",
      stopOnFocus: true
    }).showToast();
    return;
  }
  
  try {
    await api.updateTestimonial(currentTestimonial.value);
    const updatedTestimonials = await api.getAllTestimonials();
    testimonials.value = updatedTestimonials;
    bootstrap.Modal.getInstance(document.getElementById('updateTestimonialModal')).hide();
    
    // Show success toast
    Toastify({
      text: t('adminPanel.notifications.testimonialUpdated'),
      duration: 3000,
      close: true,
      gravity: "top",
      position: "right",
      backgroundColor: "#4caf50",
      stopOnFocus: true
    }).showToast();
  } catch (error) {
    console.error("Error updating testimonial:", error);
    
    // Show error toast
    Toastify({
      text: t('adminPanel.notifications.testimonialUpdateError'),
      duration: 3000,
      close: true,
      gravity: "top",
      position: "right",
      backgroundColor: "#f44336",
      stopOnFocus: true
    }).showToast();
  }
};

// Updated delete functions to use the custom modal
const deleteProject = async (projectId) => {
  // Instead of using browser confirm, use our custom modal
  confirmDeleteMessage.value = t('adminPanel.confirmDeleteProject');
  deleteItemId.value = projectId;
  deleteItemType.value = 'project';
  confirmDeleteModal.value.show();
};

const deleteTestimonial = async (testimonialId) => {
  // Instead of using browser confirm, use our custom modal
  confirmDeleteMessage.value = t('adminPanel.confirmDeleteTestimonial');
  deleteItemId.value = testimonialId;
  deleteItemType.value = 'testimonial';
  confirmDeleteModal.value.show();
};

// Add this new confirmDelete function to handle the actual deletion
const confirmDelete = async () => {
  try {
    if (deleteItemType.value === 'project') {
      // Delete project
      projects.value = projects.value.filter(project => project._id !== deleteItemId.value);
      await api.deleteProject(deleteItemId.value);
      const updatedProjects = await api.getAllProjects();
      projects.value = updatedProjects;
      
      // Show success toast
      Toastify({
        text: t('adminPanel.notifications.projectDeleted'),
        duration: 3000,
        close: true,
        gravity: "top",
        position: "right",
        backgroundColor: "#4caf50",
        stopOnFocus: true
      }).showToast();
    } else if (deleteItemType.value === 'testimonial') {
      // Delete testimonial
      testimonials.value = testimonials.value.filter(testimonial => testimonial._id !== deleteItemId.value);
      await api.deleteTestimonial(deleteItemId.value);
      const updatedTestimonials = await api.getAllTestimonials();
      testimonials.value = updatedTestimonials;
      
      // Show success toast
      Toastify({
        text: t('adminPanel.notifications.testimonialDeleted'),
        duration: 3000,
        close: true,
        gravity: "top",
        position: "right",
        backgroundColor: "#4caf50",
        stopOnFocus: true
      }).showToast();
    }
    // Hide the modal after successful deletion
    confirmDeleteModal.value.hide();
  } catch (error) {
    console.error(`Error deleting ${deleteItemType.value}:`, error);
    
    // Show error toast
    Toastify({
      text: t('adminPanel.notifications.deleteError'),
      duration: 3000,
      close: true,
      gravity: "top",
      position: "right",
      backgroundColor: "#f44336",
      stopOnFocus: true
    }).showToast();
  }
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

.table-responsive {
  overflow-x: auto;
}

.gap-2 {
  gap: 8px;
}

.img-thumbnail {
  max-width: 100px;
  height: auto;
}
</style>