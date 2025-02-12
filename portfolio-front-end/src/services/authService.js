import axios from "axios";
const API_BASE_URL = import.meta.env.API_BASE_URL;

export default {
    async register(userData) {
        return await axios.post(`${API_BASE_URL}/register`, userData);
    },

    async login(credentials) {
        const response = await axios.post(`${API_BASE_URL}/login`, credentials)
        const token = response.data.token;

        localStorage.setItem('token', token) // stores JWT in local storage
        return response.data
    },


    async logout(){
        localStorage.removeItem('token') //remove token on logout
    },


    async getUser() {
        const token = localStorage.getItem('token');
        if (!token) return null;

        try {
            const response = await axios.get(`${API_BASE_URL}/api/user`, {
                headers: { Authorization: `Bearer ${token}` }
            });
            return response.data.data;  // Returns { username, role }
        } catch (error) {
            console.error("Failed to fetch user:", error);
            localStorage.removeItem('token');
            return null;
        }
    }
};