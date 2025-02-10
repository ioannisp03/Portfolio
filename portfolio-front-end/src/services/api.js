import axios from 'axios'

const API_BASE_URL = 'http://localhost:5000'

export default {
    async sendEmail(data) {
        const response = await axios.post(`${API_BASE_URL}/send-email`, data);
        return response.data;
    },

    // Testimonials
    async getAllTestimonials() {
        const response = await axios.get(`${API_BASE_URL}/testimonials`);
        return response.data;
    },

    async addTestimonial(data) {
        const response = await axios.post(`${API_BASE_URL}/testimonials`, data);
        return response.data;
    },

    async updateTestimonial(data) {
        
        const response = await axios.put(`${API_BASE_URL}/testimonial/${data._id}`, data);
        return response.data;
    },
    

    async deleteTestimonial(id) {
        const response = await axios.delete(`${API_BASE_URL}/testimonial/${id}`);
        return response.data;
    },

    // Projects
    async getAllProjects() {
        const response = await axios.get(`${API_BASE_URL}/projects`);
        return response.data;
    },

    async updateProject(data) {
        const response = await axios.put(`${API_BASE_URL}/project/${data._id}`, data);
        return response.data;
    },

    async addProjects(data) {
        const response = await axios.post(`${API_BASE_URL}/projects`, data);
        return response.data;
    },

    async deleteProject(id) {
        const response = await axios.delete(`${API_BASE_URL}/project/${id}`);
        return response.data;
    },

    async downloadResumeCv() {
        const response = await axios.get(`${API_BASE_URL}/download-pdf`, { responseType: 'blob' });
        return response.data;
    }


};