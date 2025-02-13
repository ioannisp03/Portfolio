import axios from "axios";
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export default {
    async register(userData) {
        return await axios.post(`${API_BASE_URL}/register`, userData);
    },

    async login(credentials) {
        try {
            const response = await axios.post(`${API_BASE_URL}/login`, credentials);
            const token = response.data.token;

            if (token) {
                localStorage.setItem("token", token); // Store JWT in local storage
                window.dispatchEvent(new Event("auth-change")); // 🔥 Notify app about auth change
            }

            return response.data;
        } catch (error) {
            console.error("Login failed:", error);
            throw error; // Re-throw error to handle it in the UI
        }
    },

    async logout() {
        localStorage.removeItem("token"); // Remove token on logout
        window.dispatchEvent(new Event("auth-change")); // 🔥 Notify app about logout
    },

    async getUser() {
        const token = localStorage.getItem("token");
        if (!token) return null;

        try {
            const response = await axios.get(`${API_BASE_URL}/api/user`, {
                headers: { Authorization: `Bearer ${token}` },
            });
            return response.data.data; // Returns { username, role }
        } catch (error) {
            console.error("Failed to fetch user:", error);
            localStorage.removeItem("token"); // Remove invalid token
            window.dispatchEvent(new Event("auth-change")); // 🔥 Ensure UI updates when token is invalid
            return null;
        }
    }
};
