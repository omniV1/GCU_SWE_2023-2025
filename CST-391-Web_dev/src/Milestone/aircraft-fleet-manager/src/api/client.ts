import axios from 'axios';

/**
 * Creates an Axios instance configured with the base URL and timeout for API requests.
 * 
 * @constant
 * @type {AxiosInstance}
 * 
 * @property {string} baseURL - The base URL for the API.
 * @property {number} timeout - The timeout for API requests in milliseconds.
 */
const apiClient = axios.create({
    baseURL: 'http://localhost:5000/api',
    timeout: 5000
});

// Debug logging
apiClient.interceptors.request.use(request => {
    console.log('[API Request]:', {
        url: request.url,
        method: request.method,
        baseURL: request.baseURL,
        headers: request.headers
    });
    return request;
}, error => {
    console.error('[API Request Error]:', error);
    return Promise.reject(error);
});

apiClient.interceptors.response.use(
    response => {
        console.log('[API Response]:', {
            status: response.status,
            data: response.data
        });
        return response;
    },
    error => {
        console.error('[API Response Error]:', {
            message: error.message,
            response: error.response?.data,
            status: error.response?.status
        });
        return Promise.reject(error);
    }
);

export default apiClient;