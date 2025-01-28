import axios from 'axios'

const API_BASE_URL = 'http://localhost:5000'

export default{
    sendEmail(data){
        return axios.post(`${API_BASE_URL}/send-email`,data)
    }
}